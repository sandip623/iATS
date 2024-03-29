import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
    let loggedIn = false // replace this with actual session data to conditionally render the relative nav bar components
    return (
        <header>
            <nav>
                {
                    loggedIn==false ?
                    <ul>
                        <li><Link to="/Home">Home</Link></li>
                        <li><Link to="/Register">Register</Link></li>
                        <li><Link to="/SignIn">Sign In</Link></li>
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