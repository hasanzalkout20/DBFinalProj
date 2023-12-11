import { BrowserRouter, Route, Routes } from "react-router-dom";
import { AddCourse, AddDept, AddFaculty, AddObj, AddProgram, AddSection, AddSubObj, Home, LinkCo, AddEvalResult } from "./pages";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/add/course" element={<AddCourse />} />
          <Route path="/add/department" element={<AddDept />} />
          <Route path="/add/faculty" element={<AddFaculty />} />
          <Route path="/add/objective" element={<AddObj />} />
          <Route path="/add/program" element={<AddProgram />} />
          <Route path="/add/section" element={<AddSection />} />
          <Route path="/add/evaluation" element={<AddEvalResult />} />
          <Route path="/add/sub_objective" element={<AddSubObj />} />
          <Route path="/link/objective" element={<LinkCo />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;

