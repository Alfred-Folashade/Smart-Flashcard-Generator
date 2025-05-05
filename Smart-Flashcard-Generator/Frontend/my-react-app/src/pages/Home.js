import React, { useState } from 'react'
import styles from './Home.module.css'
import { useRef } from 'react'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Home = () => {

    const [formData, setFormData] = useState({text: ''});
    const [value, setValue] = useState('');
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
            console.log(response.data)
            navigate("/Flashcards", {state: response.data})
    
           
        } catch (error) {
            alert(error)
            console.error('Error submitting form:', error);
            alert('Failed to submit form');
        }
    }
 
    const hiddenFileInputRef = useRef(null);

    const handleClick = () => {
        hiddenFileInputRef.current.click();
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
                    <select value ={value} onChange={(e) => setValue(e.target.value)}>
                        <option value = "English">English</option>
                        <option value ="French">French</option>
                        <option value ="German">German</option>
                    </select>
                    <h2 className={styles.textBoxTitle}>Enter Your Text</h2>
                    <textarea name="text" className={styles.textInput} value={formData.message} onChange={handleChange} placeholder="Type your message here..."></textarea>
                    <button className={styles.submitButton}>Submit</button>
                </form>
            </div>
            <div className={styles.textBoxContainer} style={{marginTop: "20px"}}>
                <h2 className={styles.textBoxTitle}>Upload a file</h2>
                <div style={{height: "140px", display: "flex", justifyContent: "center", alignItems: "center"}}>
                    <div onClick={handleClick} 
                        style={{
                            width: "60px", 
                            height: "60px", 
                            borderRadius: "50%", 
                            border: "2px dashed #1a73e8", 
                            display: "flex", 
                            justifyContent: "center", 
                            alignItems: "center",
                            cursor: "pointer",
                            transition: "all 0.3s ease",
                            backgroundColor: "transparent"
                        }}
                        onMouseOver={(e) => {
                            e.currentTarget.style.backgroundColor = "rgba(26, 115, 232, 0.1)";
                            e.currentTarget.style.border = "2px solid #1a73e8";
                            e.currentTarget.style.transform = "scale(1.05)";
                        }}
                        onMouseOut={(e) => {
                            e.currentTarget.style.backgroundColor = "transparent";
                            e.currentTarget.style.border = "2px dashed #1a73e8";
                            e.currentTarget.style.transform = "scale(1)";
                        }}
                    >
                        <div style={{
                            fontSize: "30px",
                            color: "#1a73e8",
                            fontWeight: "bold",
                            lineHeight: "1",
                            transition: "all 0.3s ease"
                        }}>+</div>
                    </div>
                    <input
                    type="file"
                    ref={hiddenFileInputRef}
                    style={{ display: 'none' }}
                    />
                </div>
            </div>
        </div>
    )
  }
 
  export default Home