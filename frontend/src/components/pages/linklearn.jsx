import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { addDepartment, getAllDepartments, linkCourseToProgram } from "../../api";
import { TextField } from "../common/TextField";
import { Department, Faculty, Program, Section, Course, Objective, SubObjective, CourseObjective } from "../../models";

export const LinkLearn = () => {
// const [ departments, setDepartments ] = useState([]);
const [ id, setId ] = useState("");
const [ progid, setprogid ] = useState("");
const [ success, setSuccess ] = useState("");
//const [ objid, setobjid ] = useState("");


const handleSubmit = () => {
    linkCourseToProgram(id, progid).then(x => {
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
        <TextField label = "Course ID: " value = { id } setValue={setId}/>
        <TextField label = "Program ID: " value = { progid } setValue={setprogid}/>
        <button
            type = "button"
            onClick = {() => handleSubmit()}
        >
            Link!
        </button>
    </form>


        {/* <ul>
            {
                departments.map((department, index) => {
                    return <li key = { index }>{ department[0] }
                        <ul>
                            <li>{ department[1] }</li>
                            <li>{ department[2] }</li>
                        </ul>
                    </li>
                })
            }
        </ul> */}
        { success }
    </>
};