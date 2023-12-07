import { useState } from "react";
import { getDepartmentPrograms, getDepartmentFaculty, getEvaluation } from "../../api";
import { TextField } from "../common/TextField";
import { Department, Faculty, Program, Section, Course, Objective, CourseObjective, SubObjective} from "../../models";

export const Home = () => {
    const [department, setDepartment] = useState("");
    const [program, setProgram] = useState("");
    const [semester, setSemester] = useState("");
    const [academicYear, setAcademicYear] = useState("");
    const [programsList, setProgramsList] = useState([]);
    const [coursesList, setCoursesList] = useState([]);
    const [objectivesList, setObjectivesList] = useState([]);
    const [evaluationResults, setEvaluationResults] = useState([]);

    const handleDepartmentChange = (event) => {
        setDepartment(event.target.value);
    };

    const handleProgramChange = (event) => {
        setProgram(event.target.value);
    };

    const handleSemesterChange = (event) => {
        setSemester(event.target.value);
    };

    const handleAcademicYearChange = (event) => {
        setAcademicYear(event.target.value);
    };

    const getDepartmentPrograms = (department) => { 
        getDepartmentPrograms(department).then(x => setProgram(x));
        getDepartmentPrograms(department).then(x => console.log(x));

    }

    const getDepartmentFaculty = (department) => { 
        getDepartmentFaculty(department).then(x => setProgram(x));
        getDepartmentFaculty(department).then(x => console.log(x));

    }
    
    const getEvaluation = (department) => { 
        getEvaluation(department).then(x => setProgram(x));
        getEvaluation(department).then(x => console.log(x));

    }

    // repeat for each table
    function addDepartment(DeptID, DeptName, DeptCode) {
        const program = new Program(DeptID, DeptName, DeptCode);

    }

    function addFaculty(FacultyID, Name, Email, DeptID, Position) {
        const program = new Program(FacultyID, Name, Email, DeptID, Position);

    }

    function addProgam(ProgID, ProgName, DeptID, FacultyLeadID, FacultyLeadEmail) {
        const program = new Program(ProgID, ProgName, DeptID, FacultyLeadID, FacultyLeadEmail);

    }

    function addCourse(CourseID, DeptID, Title, Description) {
        const program = new Program(CourseID, DeptID, Title, Description);

    }

    function addSection(SecID, CourseID, Semester, Year, FacultyLeadID, EnrollCount) {
        const program = new Program(SecID, CourseID, Semester, Year, FacultyLeadID, EnrollCount);

    }

    function addObjective(ObjID, ObjCode, Description, DeptID) {
        const program = new Program(ObjID, ObjCode, Description, DeptID);

    }

    function addSubObjective(SubObjID, SubObjCode, Description, ParentObjID) {
        const program = new Program(SubObjID, SubObjCode, Description, ParentObjID);

    }

    function linkCourseObjective(CourseObjID, CourseID, ObjID) {
        const program = new Program(CourseObjID, CourseID, ObjID);

    }

// Data Entry:
//      Enter basic information about
//          Departments 
//          Faculty
//          Programs
//          Courses
//          Sections
//          Learning objectives / sub-objectives
//      Assigning courses to programs
//      Assigning learning (sub)objectives to (course, program) pairs (remember, a course can
// be associated with multiple programs, and for each program, the objectives can be
// different).
//      Enter evaluation results for a section.

// Querying. You should support the following queries: 
// Given a department:
//      List all its program
//      List all its faculty (including what program each faculty is in charge of, if there is
// one)
// Given a program:
//      List all the courses, together with the objectives/sub-objectives association with year
//      List all the objectives
// Given a semester and a program:
//      List all the evaluation results for each section. (If data for some sections has not been entered, just indicate that the information is not found)
// Given an academicyear(e.g.23-24,whichconstitutesummer23,fall23andspring24)  List all the evaluation results for each objective/sub-objective
//      For each objective/sub-objective, list the course/section that are involved in evaluating them, and list the result for each course/section.
//      For each objective/sub-objective, aggregate the result to show the number (and the percentage) of students
    return (
        <>
        
            {/* <form name="queries" id="queries">
                <TextField label="Department:" value={getDepartmentPrograms} setValue={handleDepartmentChange} />
                <button type="button" onClick={getDepartment}>
                    Get Department Details
                </button>

                <TextField label="Program:" value={program} setValue={handleProgramChange} />
                <button type="button" onClick={getProgramDetails}>
                    Get Program Details
                </button>

                <TextField label="Semester:" value={semester} setValue={handleSemesterChange} />
                <button type="button" onClick={getSemesterDetails}>
                    Get Semester Details
                </button>

                <TextField label="Academic Year:" value={academicYear} setValue={handleAcademicYearChange} />
                <button type="button" onClick={getYearlyDetails}>
                    Get Yearly Details
                </button>
            </form> */}

            {/* Display data based on queries */}
            {/* Use state variables like programsList, coursesList, objectivesList, and evaluationResults to render information */}
        </>
    );
};
