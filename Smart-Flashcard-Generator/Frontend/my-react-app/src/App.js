import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Home from './pages/Home';
import Flashcards from './pages/Flashcards'
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home/>}></Route>
        <Route path="/Flashcards" element={<Flashcards/>}></Route>
      </Routes>
    </Router>
  );
}

export default App;
