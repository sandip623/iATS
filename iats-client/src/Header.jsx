import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

const AccountDropdown = () => {
    return (
        <>
            <a href="/SignIn"><b>ACCOUNT</b></a>
            <ul class="accountDropDownContent">
                <li><a href="/Register"><b>Registration</b></a></li>
                <li><a href="/SignIn"><b>Sign In</b></a></li>
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
                        {/*
                        <li className="home"><Link to="/Home"><b>HOME</b></Link></li>
                        <li className="accountDropDown"><AccountDropdown/></li>
                        <li className="support"><Link to="/Support"><b>SUPPORT</b></Link></li>
                        */}
                        <li className="home"><a href="/Home"><b>HOME</b></a></li>
                        <li className="accountDropDown"><AccountDropdown/></li>
                        <li className="support"><a href="/Support"><b>SUPPORT</b></a></li>
                    </ul>
                    :
                    <ul>
                        <li className="home"><a href="/Home"><b>HOME</b></a></li>
                        <li className="signOut"><a href="/SignOut"><b>SIGN OUT</b></a></li>
                        <li className="support"><a href="/Support"><b>SUPPORT</b></a></li>
                    </ul>
                }
            </nav>
        </header>
    );
};

export default Header;