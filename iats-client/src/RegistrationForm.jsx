import React from 'react';
import { useState } from 'react';
import './RegistrationForm.css';

const RegistrationForm = () => {

    const [password, setPassword] = useState('');
    const [isPasswordFocused, setIsPasswordFocused] = useState(false);
    
    const handleChange = (e) => {
        setPassword(e.target.value);
    }

    const calculateStrength = () => {
        const strength = password.length > 7 ? 'strong' : password.length > 4 ? 'medium' : password.length >= 1 ? 'weak' : null;
        return strength;
    }

    const handlePasswordFocus = () => {
        setIsPasswordFocused(true);
    }

    const handlePasswordBlur = () => {
        setIsPasswordFocused(false);
    }

    return (
        <form>
            <div className="container-register">
                <h2>
                    <b>Register</b>
                </h2>
                <p>Please, fill in this form to create an account.</p>
                <hr/>
                <label htmlFor="email">
                    <b>Email</b>
                </label>
                <input type="text" placeholder="Enter Email" className="email" id="email" required/>
                <label htmlFor="psw">
                    <b>Password</b>
                </label>
                <input type="password" onChange={handleChange} onFocus={handlePasswordFocus} onBlur={handlePasswordBlur} value={password} placeholder="Enter Password" className="psw" id="psw" required/>
                
                {/* Comment: the following divs are displayed when the password input field gains focus */}
                <div className={`strength-indicator ${calculateStrength()}`}></div>
                {isPasswordFocused && (
                <div className={`password-description`}>
                    <ul>
                        <li>Must be at least 8 characters</li>
                    </ul>
                </div>)}
                
                <label htmlFor="psw-repeat">
                    <b>Repeat Password</b>
                </label>
                <input type="password" placeholder="Repeat Password" className="psw-repeat" id="psw-repeat" required/>
                <hr/>
                <p>By creating an account, you agree to our <a href="#">Terms & Privacy</a>.</p>
                <button type="submit" className="registerBtn">Register</button>
            </div>
            <div className="container-signin">
                <p>Already have an account? <a href='#'>Sign In</a>.</p>
            </div>
        </form>
    );    
};

export default RegistrationForm;