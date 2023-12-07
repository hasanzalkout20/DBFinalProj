import '../App.css';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Home, Results } from "./pages";

function App() {
  return (
    <div className = "App">
      <BrowserRouter>
        <Routes>
          <Route path = "/" element = { <Home/> }/> 
          <Route path = "/results" element = { <Results/> }/> 
          {/* add page routes */}
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
