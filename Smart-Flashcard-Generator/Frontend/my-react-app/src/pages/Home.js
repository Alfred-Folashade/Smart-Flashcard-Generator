import React, { useState } from 'react'
import styles from './Home.module.css'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Home = () => {
    const [formData, setFormData] = useState({text: ''});

    const navigate = useNavigate();

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
          });
    }

    const handleSubmit = async(e) => {
        e.preventDefault();
    
        try {
            const response = await axios.post('http://127.0.0.1:5000/read-formtext', formData, {
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            navigate("/Flashcards")
    
           
        } catch (error) {
            alert(error)
            console.error('Error submitting form:', error);
            alert('Failed to submit form');
        }
    }
    
    return (
        
        <div className={styles.page}>
            <div className={styles.cloud} style={{top: "50px", left: "50px"}}></div>
            <div className={styles.cloud} style={{top: "120px", left: "200px"}}></div>
            <div className={styles.cloud} style={{top: "200px", left: "100px"}}></div>
            <div className={styles.cloud} style={{top: "300px", left: "250px"}}></div>
            <div className={styles.cloud} style={{top: "400px", left: "50px"}}></div>
            <div className={styles.cloud} style={{top: "500px", left: "300px"}}></div>
            <div className={styles.cloud} style={{top: "600px", left: "150px"}}></div>
                   
        
            <div className={styles.textBoxContainer}>
                <form onSubmit={handleSubmit} method="post">
                    <h2 className={styles.textBoxTitle}>Enter Your Text</h2>
                    <textarea name="text" className={styles.textInput} value={formData.message} onChange={handleChange} placeholder="Type your message here..."></textarea>
                    <button className={styles.submitButton}>Submit</button>
                </form>
            </div>
        </div>
    )
  }
 
  export default Home