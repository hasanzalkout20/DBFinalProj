import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { addEvaluationResult} from "../../api";
import { TextField } from "../common/TextField";
import { Department, Faculty, Program, Section, Course, Objective, SubObjective, CourseObjective, EvalResults } from "../../models";

export const AddEvalResult= () => {
    // const [ departments, setDepartments ] = useState([]);
    const [ courseObjID, setCourseObjID ] = useState("");
    const [ sectionID, setSectionID ] = useState("");
    const [ evalMethod, setEvalMethod ] = useState("");
    const [ semester, setSemester ] = useState("");
    const [ year, setYear ] = useState("");
    const [ studentsPassed, setStudentsPassed ] = useState("");
    const [ success, setSuccess ] = useState("");

    const handleSubmit = () => {
        AddEvalResult(new Department(courseObjID, sectionID, evalMethod, semester, year, studentsPassed)).then(x => {
            // getAllDepartments().then(x => setDepartments(x));
            setSuccess("Successfully added");
        }).catch(x => {
            setSuccess("");
        })
    }

    useEffect(() => {
        // getAllDepartments().then(x => setDepartments(x));
    }, []);

    return <>
        <div>
            <h3>Input Information to Add Department:</h3>
        </div>
        
        <form name = "programs" id = "programs">
            <TextField label = "Course Objective ID: " value = { courseObjID} setValue={setCourseObjID}/>
            <TextField label = "Section ID: " value = { sectionID } setValue={setSectionID}/>
            <TextField label = "Evaluation Method: " value = { evalMethod } setValue={setEvalMethod}/>
            <TextField label = "Semester: " value = { semester } setValue={setSemester}/>
            <TextField label = "Year: " value = { year } setValue={setYear}/>
            <TextField label = "Number of students that passed: " value = { studentsPassed } setValue={setStudentsPassed}/>
            
            <button
                type = "button"
                onClick = {() => handleSubmit()}
            >
                Add Evaluation Results
            </button>
        </form>

        {/* <ul>
            {
                departments.map((department, index) => {
                    return <li key = { index }>{ department[0] }
                        <ul>
                            <li>{ department[1] }</li>
                        </ul>
                    </li>
                })
            }
        </ul> */}
        { success }
    </>
};


