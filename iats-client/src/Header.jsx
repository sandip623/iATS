import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

const Header = () => {
    let loggedIn = false // replace this with actual session data to conditionally render the relative nav bar components
    return (
        <header>
            <nav className="navbar">
                {
                    loggedIn==false ?
                    <ul>
                        <li><Link to="/Home"><b>HOME</b></Link></li>
                        <li><Link to="/Register"><b>REGISTER</b></Link></li>
                        <li><Link to="/SignIn"><b>SIGN IN</b></Link></li>
                    </ul>
                    :
                    <ul>
                        <li><Link to="/Home">Home</Link></li>
                        <li><Link to="/SignOut">Sign out</Link></li>
                    </ul>
                }
            </nav>
        </header>
    );
};

export default Header;