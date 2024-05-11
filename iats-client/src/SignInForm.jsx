import { useState } from 'react';
import './SignInForm.css';

const SigninForm = () => {
    // initialize state for input data
    const [formData, setFormData] = useState({email:'', pwd:''});

    // handler for updating input data state variable (formData)
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        // update form data by spreading existing state 
        setFormData({ ...formData, [name]: value }); 
    };

    // handler for submit action
    // async keyword used to declare an asynchronous function
    // parameter 'e' represents an event object passed to the event handler function (in this case, the form submission event)
    const handleSubmit = async (e) => {
        // stop the default behaviour of page refresh upon a submit action
        e.preventDefault();
        console.log("submission attempted...")
    };

    return (
        <form method="POST" onSubmit={handleSubmit}>
            <div className="container-signin">
                <h2><b>Sign In</b></h2>
                <p>Please, fill in this form with your account details</p>
                <hr/>
                <label htmlFor="email"><b>Email</b></label>
                <input type="text" className="email" name="email" value={formData.email} onChange={handleInputChange} placeholder="Enter Email"/>
                <label htmlFor="pwd"><b>Password</b></label>
                <input type="password" className="pwd" name="pwd" value={formData.pwd} onChange={handleInputChange} placeholder="Enter Password"/>
                <hr/>
                <button type="submit" className="registerBtn">Sign In</button>
                <p>Alternatively, <a href="Register">create a new account</a></p>
            </div>
        </form>
    );
}

export default SigninForm;