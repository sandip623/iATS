import { useEffect, useState } from 'react';
import './App.css';

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

export default App;