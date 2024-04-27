import React from 'react';
import { useState } from 'react';
import './RegistrationForm.css';

const RegistrationForm = () => {
    const [formData, setFormData] = useState({
        email:'',
        password:''
    })
    const [inputPassword, setInputPassword] = useState('');
    const [isPasswordFocused, setIsPasswordFocused] = useState(false);
    const [message, setMessage] = useState(''); // for dynamically handling submission feedback message...#
    const [inputPasswordRe, setInputPasswordRe] = useState('');
    const [isPasswordMatch, setIsPasswordMatch] = useState(false);

    // specifically for handling changes on password input field
    const handleChange = (e) => {
        setInputPassword(e.target.value);
        const {name, value} = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    }

    const calculateStrength = () => {
        const strength = inputPassword.length > 7 ? 'strong' : inputPassword.length > 4 ? 'medium' : inputPassword.length >= 1 ? 'weak' : null;
        return strength;
    }

    const handlePasswordFocus = () => {
        setIsPasswordFocused(true);
    }

    const handlePasswordBlur = () => {
        setIsPasswordFocused(false);
    }

    const handleChangeFormData = (e) => {
        const {name, value} = e.target;
        setFormData(prevState => ({
            ...prevState, // spread operator to quickly copy previous state - good practice when modifying state objects 
            [name]: value // update the relative property (the variables 'name' and 'value' are key value obtained from the relative user field input)
        }));
    }

    /* submission feedback functions */
    const showMessage = (text) => {
        setMessage(text);
        // clear the message after 3 seconds
        setTimeout(() => {
            setMessage('');
        }, 9000);
    }

    // **** event handler function to check if the input passwords match ***
    
    // update re-password state
    const handleChangePasswordRe = (e) => {
        setInputPasswordRe(e.target.value);
    }

    const checkPasswords = () => {
        if (formData.password !== inputPasswordRe) {
            setIsPasswordMatch(false);
            showMessage("Passwords do not match.");
            return isPasswordMatch;
        }
        setIsPasswordMatch(true);
        return isPasswordMatch;
    }

    /* function to submit form data */
    const handleSubmit = async (e) => {
        // prevent default form submission behaviour (i.e., page reload)
        e.preventDefault();
        // If the passwords do not match, the function stops executing further and prevents the form from being submitted.
        if (!checkPasswords()) {
            return;
        }
        try {
            // send a POST request to the relative flask server endpoint
            const response = await fetch('http://localhost:5000/submit-registration', 
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            // get the response body (http status-code returned from flask endpoint)
            const responseBody = await response.json();

            if (responseBody == 200) {
                showMessage("Your account was successfully registered...");
            } else if (responseBody == 406 || responseBody == 500) {
                showMessage("Unable to create the account: "+responseBody);
            } else {
                showMessage("Something went wrong. Please, try again later.");
            }
        } catch (error) {
            console.error('Error submitting registration: ', error);
        }
    }

    return (
        <form onSubmit={handleSubmit} method="POST">
            <div className="container-register">
                <h2><b>Register</b></h2>
                <p>Please, fill in this form to create an account.</p>
                <hr/>
                <label htmlFor="email"><b>Email</b></label>
                <input type="text" placeholder="Enter Email" className="email" id="email" name="email" required onChange={handleChangeFormData} />
                <label htmlFor="psw"><b>Password</b></label>
                <input type="password" onChange={handleChange} onFocus={handlePasswordFocus} onBlur={handlePasswordBlur} value={inputPassword} placeholder="Enter Password" className="psw" id="psw" name="password" required/>
                {/* Comment: the following divs are displayed when the password input field gains focus */}
                <div className={`strength-indicator ${calculateStrength()}`}></div>
                {isPasswordFocused && (
                <div className={`password-description`}>
                    <ul>
                        <li>Must be at least 8 characters</li>
                    </ul>
                </div>)}   
                <label htmlFor="psw-repeat"><b>Repeat Password</b></label>
                <input type="password" placeholder="Repeat Password" className="psw-repeat" id="psw-repeat" onChange={handleChangePasswordRe} required/>
                <hr/>
                <p>By creating an account, you agree to our <a href="#">Terms & Privacy</a>.</p>
                <button type="submit" className="registerBtn">Register</button>
                {/* Comment: the following div is displayed upon submission... */}
                {message && <div className={`message ${message.includes('successful') ? 'success' : 'error'}`}>{message}</div>}
                </div>
            <div className="container-signin">
                <p>Already have an account? <a href='/SignIn'>Sign In</a>.</p>
            </div>
        </form>

    );    
};

export default RegistrationForm;