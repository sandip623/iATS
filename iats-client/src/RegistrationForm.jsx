import React from 'react';
import { useState } from 'react';

const RegistrationForm = () => {
    return (
        <form method="POST">
            <div class="container">
                <h2>Registration Form</h2>
                <label for="email"><b>Email</b></label>
                <input type="text" placeholder="Email"/>
            </div>
        </form>
    );    
};

export default RegistrationForm;