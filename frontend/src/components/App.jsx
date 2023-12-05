import '../App.css';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Home } from "./pages";

function App() {
  return (
    <div className = "App">
      <BrowserRouter>
        <Routes>
          <Route path = "/" element = { <Home/> }/> 
          <Route path = "/login" element = { <Home/> }/> 
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
