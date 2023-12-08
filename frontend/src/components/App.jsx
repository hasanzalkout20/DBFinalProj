import '../App.css';
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { AddCourse, AddDept, AddFaculty, AddObj, AddProgram, AddSection, AddSubObj, Home, LinkLearn, LinkCo } from "./pages";

function App() {
  return (
    <div className = "App">
      <BrowserRouter>
        <Routes>
          <Route path = "/" element = { <Home/> }/> 
          <Route path = "/add/course" element = { <AddCourse/> }/>
          <Route path = "/add/department" element = { <AddDept/> }/>
          <Route path = "/add/faculty" element = { <AddFaculty/> }/>
          <Route path = "/add/objective" element = { <AddObj/> }/>
          <Route path = "/add/program" element = { <AddProgram/> }/>
          <Route path = "/add/section" element = { <AddSection/> }/>
          <Route path = "/add/sub_objective" element = { <AddSubObj/> }/>
          <Route path = "/link/program" element = { <LinkLearn/> }/>
          <Route path = "/link/objective" element = { <LinkCo/> }/>
          {/* add page routes */}
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
