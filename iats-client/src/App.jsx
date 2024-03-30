import React, { useEffect, useState } from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './Header';
import RegistrationForm from './RegistrationForm';

/*
const fetchData = async () => {
    try {
        const response = await fetch("http://127.0.0.1:5000/");
        const data = await response.json();
        return data;        
    } catch (error) {
        return error();
    }
}

function App() {
    const [data, setData] = useState(null);
    // useEffect hook handles side-effect
    useEffect(() => {
        fetchData()
            .then(data => setData(data))
            .catch(error => console.log('Error: ', error));
    }, []);
    return (
        <div>
            <p>Hello World!</p>
            <p>Data: {data}</p>
        </div>
        );
}
*/

const App = () => {
    return (
        <Router>
            <div>
                <Header />
                    <Routes>
                        <Route path="/" element={<p>Hello World!</p>}/>
                        <Route path="/Home" element={<p>Home Page</p>}/>
                        <Route path="/SignIn" element={<p>Sign In Page</p>}/>
                        <Route path="/register" element={<RegistrationForm />}/>
                    </Routes>
            </div>
        </Router>
    );
}

export default App;