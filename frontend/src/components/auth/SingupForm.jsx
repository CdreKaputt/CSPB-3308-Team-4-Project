import { useState } from "react";
import { useNavigate } from "react-router-dom";

function SignupForm( { onSignupSuccess }) {
    const [formData, setFormData] = useState({ 
        username: '',
        email: '',
        first_name: '',
        last_name: '', 
        password: ''
    });

    const navigate = useNavigate()

    const handleSubmit = async (e) => {
        e.preventDefault();

        const response = await fetch("/api/users/", {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData)
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem('token', data.access_token)
            localStorage.setItem('refresh-token', data.refresh_token);
            // onSignupSuccess(data.user);
            navigate("/login")
        } else {
            alert("Oops! Something went wrong. Please try again.");
        }
    };

    return (
        <>
            <div className="signup-form-container">
                <form className="signup-form" onSubmit={handleSubmit}>
                    <input
                        type="text"
                        placeholder="username"
                        onChange={(e) => setFormData({ ...formData, username: e.target.value })}
                    />
                    <input
                        type="email"
                        placeholder="email"
                        onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                    />
                    <input
                        type="text"
                        placeholder="First Name"
                        onChange={(e) => setFormData({ ...formData, first_name: e.target.value })}
                    />
                    <input
                        type="text"
                        placeholder="Last Name"
                        onChange={(e) => setFormData({ ...formData, last_name: e.target.value })}
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

export default SignupForm; 