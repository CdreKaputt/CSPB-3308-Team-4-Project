import { useState } from "react";
import './auth.css' 
import { useNavigate } from "react-router-dom";

function LoginForm( { onLoginSuccess }) {
    const [formData, setFormData] = useState({ username: '', password: ''});
    const navigate = useNavigate()

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await fetch("/api/auth/login", {
            method: "POST",
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify(formData)
        });

        if (response.ok) {
            const data = await response.json();

            localStorage.setItem('token', data.access_token)
            localStorage.setItem('refresh-token', data.refresh_token);

            onLoginSuccess(data.user.username);
            navigate('/')
        } else {
            alert("Oops! Something went wrong. Please try again.");
        }
    };

    return (
        <>
            <div className="login-form-container">
                <form className="login-form" onSubmit={handleSubmit}>
                    <input 
                        type="text" 
                        placeholder="username"
                        onChange={(e) => setFormData({...formData, username: e.target.value})}
                    />
                    <input
                        type="password"
                        placeholder="password"
                        onChange={(e) => setFormData({ ...formData, password: e.target.value })}
                    />
                    <button type="submit">Login</button>
                </form>
            </div>
        </>
    )
}

export default LoginForm; 