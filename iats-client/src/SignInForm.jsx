import './SignInForm.css';

const SigninForm = () => {
    return (
        <form method="POST">
            <div className="container-signin">
                <h2><b>Log In</b></h2>
                <p>Sign In </p>
                <hr/>
                <label htmlFor="email">Email</label>
                <input type="text"/>
            </div>
        </form>
    );
}

export default SigninForm;