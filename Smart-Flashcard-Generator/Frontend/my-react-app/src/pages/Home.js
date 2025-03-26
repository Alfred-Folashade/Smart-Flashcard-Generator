import React from 'react'
import styles from './Home.modules.css'
const Home = () => {
    return (
        
        <div>
            <div className="cloud" style={{top: "50px", left: "50px"}}></div>
            <div className="cloud" style={{top: "120px", left: "200px"}}></div>
            <div className="cloud" style={{top: "200px", left: "100px"}}></div>
            <div className="cloud" style={{top: "300px", left: "250px"}}></div>
            <div className="cloud" style={{top: "400px", left: "50px"}}></div>
            <div className="cloud" style={{top: "500px", left: "300px"}}></div>
            <div className="cloud" style={{top: "600px", left: "150px"}}></div>
                   
        
            <div class="text-box-container">
                <form action="" method="post">
                <h2 class="text-box-title">Enter Your Text</h2>
                <textarea  class="text-input" placeholder="Type your message here..."></textarea>
                <button class="submit-button">Submit</button>
                </form>
            </div>
        </div>
    )
  }
 
  export default Home