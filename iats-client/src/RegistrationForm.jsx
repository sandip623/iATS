import React from 'react';
import { useState } from 'react';
import './RegistrationForm.css';

const RegistrationForm = () => {

    return (
        <form>
            <div className="container-register">
                <h2>Registration Form</h2>
                <p>Please, fill in this form to create an account.</p>
                <hr/>
                <label htmlFor="email"><b>Email</b></label>
                <input type="text" placeholder="Enter Email" className="email" id="email" required/>
                <label htmlFor="psw"><b>Password</b></label>
                <input type="password" placeholder="Enter Password" className="psw" id="psw" required/>
                <label htmlFor="psw-repeat"><b>Repeat Password</b></label>
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