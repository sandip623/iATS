import './SignInForm.css';

const SigninForm = () => {
    return (
        <form method="POST">
            <div className="container-signin">
                <h2><b>Sign In</b></h2>
                <p>Please, fill in this form with your account details</p>
                <hr/>
                <label htmlFor="email"><b>Email</b></label>
                <input type="text" className="email"/>
                <label htmlFor="pwd"><b>Password</b></label>
                <input type="password" className="pwd"/>
                <hr/>
                {/* we want to rename the button class for signin */}
                <button type="submit" className="registerBtn"/>
            </div>
        </form>
    );
}

export default SigninForm;