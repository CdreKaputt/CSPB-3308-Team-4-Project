import { useEffect, useState } from 'react'
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import './App.css' 
import Navbar from './components/navigation/Navbar'
import LoginForm from './components/auth/LoginForm'
import SignupForm from './components/auth/SingupForm'

function App() {
    const [user, setUser] = useState(null);

    useEffect(() => {
        const token = localStorage.getItem('token');

        if (token) { // go get the current user from db on refresh
            fetch('/api/users/', {
                headers: { 
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                }
            })
            .then(res => res.ok ? res.json() : Promise.reject())
            .then(data => setUser(data.username))
            .catch(() => {
                localStorage.removeItem('token');
                localStorage.removeItem('refresh-token');
                setUser(null);
            })
        }
    }, [])

    console.log("App Prop User:", user);

    return (
        <>
            <Router>
                <Navbar user={user} onLogoutSuccess={() => setUser(null)} />

                <main>
                    <Routes>
                        {/* Home Page just inline html for now */}
                        <Route path="/" element={
                            user ? <h2>Welcome Back {user}!</h2> : <h2>Please Log In or Sign Up</h2>
                        } />

                        <Route path="/login" element={
                            !user ? <LoginForm onLoginSuccess={(u) => setUser(u)} /> : <Navigate transition to="/" />
                        } />
                        
                        <Route path="/signup" element={
                            !user ? <SignupForm onSignupSuccess={(u) => setUser(u)} /> : <Navigate to="/" />
                        } />
                    </Routes>
                </main>
            </Router>
        </>
    )
}

export default App
