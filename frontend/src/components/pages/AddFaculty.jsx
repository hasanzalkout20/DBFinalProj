import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { addFaculty, getDepartmentFaculty } from "../../api";
import { TextField } from "../common/TextField";
import { Department, Faculty, Program, Section, Course, Objective, SubObjective, CourseObjective } from "../../models";

export const AddFaculty = () => {
    const [ faculty, setFaculty ] = useState([]);
    const [ id, setId ] = useState("");
    const [ name, setName ] = useState("");
    const [ email, setEmail ] = useState("");
    // changed: const [ deptID, setDeptId ] = useState("");
    const [ deptCode, setDeptCode ] = useState("");
    const [ position, setPosition ] = useState("");
    const [ success, setSuccess ] = useState("");
    

    const handleSubmit = () => {
        addFaculty(new Faculty(id, name, email, deptCode, position)).then(x => {
            // getAllDepartments().then(x => setDepartments(x));
            setSuccess("Successfully added");
        }).catch(x => {
            setSuccess("");
        })
    }
 

    return <>
        <div>
            <h3>Input Information to Add Faculty:</h3>
        </div>
        
        <form name = "faculty" id = "faculty">
            <TextField label = "Faculty ID: " value = { id } setValue={setId}/>
            <TextField label = "Name: " value = { name } setValue={setName}/>
            <TextField label = "Email: " value = { email } setValue={setEmail}/>
            <TextField label = "Department Code: " value = { deptCode } setValue={setDeptCode}/>
            <TextField label = "Position: " value = { position } setValue={setPosition}/>
            
            <button
                type = "button"
                onClick = {() => {
                    handleSubmit()
                }}
            >
                Add Faculty
            </button>
        </form>

        {success}
    </>
};
