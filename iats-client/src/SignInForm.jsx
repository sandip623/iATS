import { useState } from 'react';
import './SignInForm.css';

const SigninForm = () => {
    // initialize state for input data
    const [formData, setFormData] = useState({email:'', pwd:''});

    // handler for updating input data state variable (formData)
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        // update form data by spreading existing state (spread operator in react is used for update or merge objects and arrays)
        setFormData({ ...formData, [name]: value }); 
    };

    return (
        <form method="POST">
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