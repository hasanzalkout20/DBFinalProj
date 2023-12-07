import '../App.css';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { AddDept, Home, Results } from "./pages";

function App() {
  return (
    <div className = "App">
      <BrowserRouter>
        <Routes>
          <Route path = "/" element = { <Home/> }/> 
          <Route path = "/results" element = { <Results/> }/> 
          <Route path = "/add/department" element = { <AddDept/> }/>
          {/* add page routes */}
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
