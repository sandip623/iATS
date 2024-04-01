import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

const AccountDropdown = () => {
    return (
        <>
            <Link to="/SignIn"><b>ACCOUNT</b></Link>
            <ul class="accountDropDownContent">
                <li><Link to="/Register"><b>Registration</b></Link></li>
                <li><Link to="/SignIn"><b>Sign In</b></Link></li>
            </ul>
        </>
    )
}

const Header = () => {
    let loggedIn = false // replace this with actual session data to conditionally render the relative nav bar components
    return (
        <header>
            <nav className="navbar">
                {
                    loggedIn==false ?
                    <ul>
                        <li className="home"><Link to="/Home"><b>HOME</b></Link></li>
                        {/* 
                        <li><Link to="/Register"><b>REGISTER</b></Link></li>
                        <li><Link to="/SignIn"><b>SIGN IN</b></Link></li>
                        */}
                        <li className="accountDropDown"><AccountDropdown/></li>
                        <li className="support"><Link to="/Support"><b>SUPPORT</b></Link></li>
                    </ul>
                    :
                    <ul>
                        <li className="home"><Link to="/Home"><b>HOME</b></Link></li>
                        <li className="signOut"><Link to="/SignOut"><b>SIGN OUT</b></Link></li>
                        <li className="support"><Link to="/Support"><b>SUPPORT</b></Link></li>
                    </ul>
                }
            </nav>
        </header>
    );
};

export default Header;