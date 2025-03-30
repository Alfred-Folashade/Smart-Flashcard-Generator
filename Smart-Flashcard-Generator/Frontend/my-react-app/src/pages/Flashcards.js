import React, { useState } from 'react'






function Flashcards() {
  const { useState } = React;

    // Sample flashcards data
    const flashcardsData = [
      { word: "Bonjour", definition: "Hello (in French)" },
      { word: "Gracias", definition: "Thank you (in Spanish)" },
      { word: "Au revoir", definition: "Goodbye (in French)" },
      { word: "Por favor", definition: "Please (in Spanish)" },
    ];
   // Flashcard component that handles the flip animation
   const Flashcard = ({ flashcard, flipped, onFlip }) => {
    return (
      <div className={`flashcard ${flipped ? "flipped" : ""}`} onClick={onFlip}>
        <div className="front">
          {flashcard.word}
        </div>
        <div className="back">
          {flashcard.definition}
        </div>
      </div>
    );
  };

  // Main App component
 
    const [currentIndex, setCurrentIndex] = useState(0);
    const [flipped, setFlipped] = useState(false);
    const totalCards = flashcardsData.length;

    const handleFlip = () => setFlipped(!flipped);
    const handleNext = () => {
      setCurrentIndex((currentIndex + 1) % totalCards);
      setFlipped(false);
    };

    const progressPercent = ((currentIndex) / totalCards) * 100;

    
     
  

  // Render the React App into the DOM
  
  return (
    <div>
    <div class="cloud" style={{top: "50px", left: "50px"}}></div>
    <div class="cloud" style={{top: "120px", left: "200px"}}></div>
    <div class="cloud" style={{top: "200px", left: "100px"}}></div>
    <div class="cloud" style={{top: "300px", left: "250px"}}></div>
    <div class="cloud" style={{top: "400px", left: "50px"}}></div>
    <div class="cloud" style={{top: "500px", left: "300px"}}></div>
    <div class="cloud" style={{top: "600px", left: "150px"}}></div>
    <div className="flashcard-container">
        <div className="progress-bar">
          <div className="progress-bar-fill" style={{ width: progressPercent + '%' }}></div>
        </div>
        <Flashcard 
          flashcard={flashcardsData[currentIndex]} 
          flipped={flipped} 
          onFlip={handleFlip} 
        />
        <div>
          {flipped ? (
            <button className="btn" onClick={handleNext}>Next Card</button>
          ) : (
            <button className="btn" onClick={handleFlip}>Show Answer</button>
          )}
        </div>
        <p>{currentIndex + 1} / {totalCards}</p>
      </div>
    
    <div id="root"></div>
    
    
 
      </div>
  );
}

export default Flashcards;
