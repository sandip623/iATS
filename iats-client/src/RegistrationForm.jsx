import React from 'react';
import { useState } from 'react';
import './RegistrationForm.css';

const RegistrationForm = () => {

    return (
        <form className="registration-form" method="POST">
            <div className="container">
                <h2>Registration Form</h2>
                <label for="email"><b>Email</b></label>
                <input type="text" placeholder="Email"/>
            </div>
        </form>
    );    
};

export default RegistrationForm;