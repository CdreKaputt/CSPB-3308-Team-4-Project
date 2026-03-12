import React, { useEffect } from "react";
import { NavLink, useNavigate } from "react-router-dom";

function Navbar({ user, onLogoutSuccess }) {
    const navigate = useNavigate();

    console.log("Navbar Prop User:", user);
    
    const handleLogout = () => {
        const token = localStorage.getItem("access_token")
        fetch("/api/auth/logout", {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
                 'Authorization': `Bearer ${token}`
            }
        })
        localStorage.removeItem('token');
        localStorage.removeItem('refresh-token');

        onLogoutSuccess();
        navigate("/login")
        alert("Successfully Logged Out")
        
    }

    return (
        <nav >
            <div>
                <h1>Flake</h1>
            </div>

            <ul>
                {user ? (
                    // Display welcome when logged in
                    <>
                        <li>Welcome, {user}!</li>
                        <li>
                            <button onClick={handleLogout}>
                                Logout
                            </button>
                        </li>
                    </>
                ): (
                    <>
                        <li><NavLink to="/login">Login</NavLink></li>
                        <li><NavLink to="/signup">Signup</NavLink></li>
                    </>
                )}
            </ul>
        </nav>
    )
}

export default Navbar;