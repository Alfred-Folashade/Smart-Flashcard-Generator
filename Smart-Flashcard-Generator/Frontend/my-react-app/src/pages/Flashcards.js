import React, { useState } from 'react';
import styles from './Flashcards.module.css';
import { useLocation } from "react-router-dom";



/*
const flashcardsData = [
  { word: "Bonjour", definition: "Hello (in French)" },
  { word: "Gracias", definition: "Thank you (in Spanish)" },
  { word: "Au revoir", definition: "Goodbye (in French)" },
  { word: "Por favor", definition: "Please (in Spanish)" },
];
*/

// Flashcard component that handles the flip animation
const Flashcard = ({ flashcard, flipped, onFlip, index }) => {
  return (
    <div className={`${styles.flashcard} ${flipped ? styles.flipped : ""}`} onClick={onFlip}>
      
      <div className={styles.front}>
        {flashcard.word}
      </div>
      <div className={styles.back}>
        {flashcard.definition}
      </div>
    </div>
  );
};

// Main Flashcards component
const Flashcards = () => {
  // Sample flashcards data
  const location = useLocation();
  const flashcardsData = (location.state);
  console.log(flashcardsData)
  const [currentIndex, setCurrentIndex] = useState(0);
  const [flipped, setFlipped] = useState(false);
  const totalCards = flashcardsData.length;

  const handleFlip = () => setFlipped(!flipped);
  const handleNext = () => {
    setCurrentIndex((currentIndex + 1) % totalCards);
    setFlipped(false);
  };

  const progressPercent = ((currentIndex) / totalCards) * 100;

  return (
    <div className={styles.page}>
      {/* Static Clouds */}
      <div className={styles.cloud} style={{ top: '50px', left: '50px' }}></div>
      <div className={styles.cloud} style={{ top: '120px', left: '200px' }}></div>
      <div className={styles.cloud} style={{ top: '200px', left: '100px' }}></div>
      <div className={styles.cloud} style={{ top: '300px', left: '250px' }}></div>
      <div className={styles.cloud} style={{ top: '400px', left: '50px' }}></div>
      <div className={styles.cloud} style={{ top: '500px', left: '300px' }}></div>
      <div className={styles.cloud} style={{ top: '600px', left: '150px' }}></div>

      <div className={styles.flashcardContainer}>
        <div className={styles.progressBar}>
          <div className={styles.progressBarFill} style={{ width: progressPercent + '%' }}></div>
        </div>
       
            
        
        <Flashcard 
          flashcard={flashcardsData[currentIndex]} 
          flipped={flipped} 
          onFlip={handleFlip} 
          index={currentIndex}
          
        />
        <div>
          {flipped ? (
            <button className={styles.btn} onClick={handleNext}>Next Card</button>
          ) : (
            <button className={styles.btn} onClick={handleFlip}>Show Answer</button>
          )}
        </div>
        
        <p>{currentIndex + 1} / {totalCards}</p>
      </div>
    </div>
  );
};

export default Flashcards;