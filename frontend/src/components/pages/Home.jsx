import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { addDepartment, addFaculty, addProgram, addCourse, addSection, addObjective, addSubObjective, linkCourseObjective, getDepartmentPrograms, getDepartmentFaculty, getEvaluation, getProgramCoursesObjectives, getProgramObjectives, getEvaluationYear } from "../../api";
import { TextField } from "../common/TextField";
import { Department, Faculty, Program, Section, Course, Objective, CourseObjective, SubObjective} from "../../models";


export const Home = () => {
    const [department, setDepartment] = useState("");
    const [program, setProgram] = useState("");
    const [ faculty, setFaculty ] = useState([]);
    const [semester, setSemester] = useState("");
    const [year, setYear] = useState("");
    const [academicYear, setAcademicYear] = useState("");
    const [programsList, setProgramsList] = useState([]);
    const [coursesList, setCoursesList] = useState([]);
    const [objectivesList, setObjectivesList] = useState([]);
    const [objectivesList2, setObjectivesList2] = useState([]);
    const [evaluationResults, setEvaluationResults] = useState([]);

    const navigate = useNavigate();

    const handleDepartmentSubmit = (department) => { 
        getDepartmentPrograms(department).then(x => setProgramsList(x));
        getDepartmentFaculty(department).then(x => setFaculty(x));
    }

    const handleProgramSubmit = (program) => { 
        getProgramCoursesObjectives(program).then(x => setCoursesList(x));
        getProgramObjectives(program).then(x => setObjectivesList(x));
    }

    const handleSemesterProgramSubmit = (semester, year, program) => {
        getEvaluation(semester, program, year).then(x => setEvaluationResults(x));
    }


    const handleAcademicYearSubmit = (year) => {
        getEvaluationYear(year).then(x => setObjectivesList2(x));
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
                
        <div>
            <h3> Add:</h3>
        </div>
    
        <form name = "programs" id = "programs">
            <button
                type = "button"
                onClick = {() => {
                    // getPrograms(department);
                    navigate("/add/department");
                }}
            >
                Add Department
            </button>

            <button
                type = "button"
                onClick = {() => {
                    // getPrograms(department)
                    navigate("/add/faculty");
                }}
            >
                Add Faculty
            </button>

            <button
                type = "button"
                onClick = {() => {
                    // getPrograms(department)
                    navigate("/add/program");
                }}
            >
                Add Program
            </button>

            <button
                type = "button"
                onClick = {() => {
                    // getPrograms(department)
                    navigate("/add/course");
                }}
            >
                Add Course
            </button>

            <button
                type = "button"
                onClick = {() => {
                    //getPrograms(department)
                    navigate("/add/section");
                }}
            >
                Add Section
            </button>

            <button
                type = "button"
                onClick = {() => {
                    //getPrograms(department)
                    navigate("/add/objective");
                }}
            >
                Add Objective
            </button>

            <button
                type = "button"
                onClick = {() => {
                    //getPrograms(department)
                    navigate("/add/sub_objective");
                }}
            >
                Add Sub-Objective
            </button>

        </form>

        <div>
            <h3>Assign:</h3>
        </div>

        <form name = "programs" id = "programs"> 
            <button
                type = "button"
                onClick = {() => {
                    navigate("/link/objective")
                }}
            >
                Assign a Learning Objective
            </button>

            <button
                type = "button"
                onClick = {() => {
                    navigate("/link/program")
                }}
            >
                Assign a Course
            </button>

        </form>
        
        <form name = "departments" id = "departments">
            <TextField label = "Department : " value = {department } setValue={setDepartment}/>

            <button
                type = "button"
                onClick = {() => {
                    handleDepartmentSubmit(department)
                }}
            >
                Submit
            </button>
        </form>

        <div>
            Programs:
            <ul>
                {
                    programsList.map((program, i) => {
                        return <li key = { i }>
                            { program }
                        </li>
                    })
                }
            </ul>
        </div>

        <div>
            Faculty:
            <ul>
                {
                    faculty.map((f, i) => {
                        return <li key = { i }>
                            { f }
                        </li>
                    })
                }
            </ul>
        </div>
        
        
        <form name = "departments" id = "departments">
            <TextField label = "Program : " value = {program } setValue={setProgram}/>

            <button
                type = "button"
                onClick = {() => {
                    handleProgramSubmit(program)
                }}
            >
                Submit
            </button>
        </form>

        <div>
            Courses:
            <ul>
                {
                    coursesList.map((program, i) => {
                        return <li key = { i }>
                            { program }
                        </li>
                    })
                }
            </ul>
        </div>

        <div>
            Objectives:
            <ul>
                {
                    objectivesList.map((f, i) => {
                        return <li key = { i }>
                            { f }
                        </li>
                    })
                }
            </ul>
        </div>

        
        <form name = "departments" id = "departments">
            <TextField label = "Semester : " value = {semester } setValue={setSemester}/>
            <TextField label = "Year : " value = {year } setValue={setYear}/>
            <TextField label = "Program : " value = {program } setValue={setProgram}/>

            <button
                type = "button"
                onClick = {() => {
                    handleSemesterProgramSubmit(semester, year, program)
                }}
            >
                Submit
            </button>
        </form>

        <div>
            Evaluation Results for each section:
            <ul>
                {
                    evaluationResults.map((program, i) => {
                        return <li key = { i }>
                            { program }
                        </li>
                    })
                }
            </ul>
        </div>

       

        

        {/* <TextField label = "Academic year : " value = {name } setValue={setName}/> */}
        <form name = "departments" id = "departments">
            <TextField label = "Academic year : " value = {academicYear } setValue={setAcademicYear}/>

            <button
                type = "button"
                onClick = {() => {
                    handleAcademicYearSubmit(academicYear)
                }}
            >
                Submit
            </button>
        </form>

        <div>
            Evaluation Results for each objective/sub-objective:
            <ul>
                {
                    objectivesList2.map((program, i) => {
                        return <li key = { i }>
                            { program }
                        </li>
                    })
                }
            </ul>
        </div>

    </>

        
        );

};
