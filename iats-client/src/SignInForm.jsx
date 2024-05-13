import { useState } from 'react';
import './SignInForm.css';
import BASE_URL from './config.js';

const SigninForm = () => {
    // initialize state for input data
    const [formData, setFormData] = useState({email:'', pwd:''});
    // set regex variables to be used in input validation
    const regex_email = /^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,5})$/;
    const regex_pwd = /^([a-z0-9_\.\-\@\!\#\*]+)$/;

    // handler for updating input data state variable (formData)
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        // update form data by spreading existing state (if input passes validation)
        setFormData({ ...formData, [name]: value }); 
    };

    // handler for submit action
    // async keyword used to declare an asynchronous function
    // parameter 'e' represents an event object passed to the event handler function (in this case, the form submission event)
    const handleSubmit = async (e) => {
        // stop the default behaviour of page refresh upon a submit action
        e.preventDefault();
        
        if (regex_email.test(formData.email)) {
            console.log('valid email')
        }

        try {
            // send a http POST request containing submission data to the backend server
            const response = await fetch(`${BASE_URL}/submit-signin`,
                {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'},
                    body: JSON.stringify(formData)
                });

        } catch (error) {
            console.error('Error when signing in: ', error);
        };
    };

    return (
        <form method="POST" onSubmit={handleSubmit}>
            <div className="container-signin">
                <h2><b>Sign In</b></h2>
                <p>Please, fill in this form with your account details</p>
                <hr/>
                <label htmlFor="email"><b>Email</b></label>
                <input type="text" className="email" name="email" value={formData.email} onChange={handleInputChange} placeholder="Enter Email" required/>
                <label htmlFor="pwd"><b>Password</b></label>
                <input type="password" className="pwd" name="pwd" value={formData.pwd} onChange={handleInputChange} placeholder="Enter Password" required/>
                <hr/>
                <button type="submit" className="registerBtn">Sign In</button>
                <p>Alternatively, <a href="Register">create a new account</a></p>
            </div>
        </form>
    );
}

export default SigninForm;