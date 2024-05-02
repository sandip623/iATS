import React, { useEffect, useState } from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './Header';
import RegistrationForm from './RegistrationForm';
import SigninForm from './SignInForm';

const App = () => {
    return (
        <Router>
            <div>
                <Header />
                <div style= {{paddingTop: '90px'}}> {/* Add padding to create space - to stop the navbar overlapping the top of each page */}
                    <Routes>
                        <Route path="/" element={<p>Hello World!</p>}/>
                        <Route path="/Home" element={<p>Home Page</p>}/>
                        <Route path="/Signin" element={<SigninForm/>}/>
                        <Route path="/Register" element={<RegistrationForm />}/>
                    </Routes>
                </div>    
            </div>
        </Router>
    );
}

export default App;