import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { addProgram, getDepartmentPrograms } from "../../api";
import { TextField } from "../common/TextField";
import { Department, Faculty, Program, Section, Course, Objective, SubObjective, CourseObjective } from "../../models";

export const AddProgram = () => {
    const [ programs, setPrograms ] = useState([]);
    const [ id, setID ] = useState("");
    const [ name, setName ] = useState("");
    const [ deptID, setDeptID ] = useState("");
    const [ facultyLeadID, setFacultyLeadID ] = useState("");
    const [ facultyLeadEmail, setFacultyLeadEmail ] = useState("");
    const [ success, setSuccess ] = useState("");

    const handleSubmit = () => {
        addProgram(new Program(id, name, deptID, facultyLeadID, facultyLeadEmail)).then(x => {
            // getAllDepartments().then(x => setDepartments(x));
            setSuccess("Successfully added");
        }).catch(x => {
            setSuccess("");
        })
    }


    return <>
        <div>
            <h3>Input Information to Add Programt:</h3>
        </div>
        
        <form name = "programs" id = "programs">
        <TextField label = "Program ID: " value = { id } setValue={ setID }/>
            <TextField label = "Program Name: " value = { name } setValue={setName}/>
            <TextField label = "Department ID: " value = { deptID } setValue={setDeptID}/>
            <TextField label = "Faculty Lead ID: " value = { facultyLeadID } setValue={setFacultyLeadID}/>
            <TextField label = "Faculty Lead Email: " value = { facultyLeadEmail } setValue={setFacultyLeadEmail}/>
            <button
                type = "button"
                onClick = {() => {
                    handleSubmit();
                }}
            >
                Add Program
            </button>
        </form>

        {success}
    </>
};
