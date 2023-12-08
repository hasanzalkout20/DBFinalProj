import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { addObjective, getAllObjectives } from "../../api";
import { TextField } from "../common/TextField";
import { Department, Faculty, Program, Section, Course, Objective, SubObjective, CourseObjective } from "../../models";

export const AddObj = () => {
    const [ objectives, setObjectives ] = useState([]);
    const [ id, setId ] = useState("");
    const [ code, setCode ] = useState("");
    const [ description, setDescription ] = useState("");
    const [ deptID, setDeptID ] = useState("");
    const [ success, setSuccess ] = useState("");


    const handleSubmit = () => {
        addObjective(new Objective(id, code, description, deptID)).then(x => {
            // getAllDepartments().then(x => setDepartments(x));
            setSuccess("Successfully added");
        }).catch(x => {
            setSuccess("");
        })
    }

    return <>
        <div>
            <h3>Input Information to Add Objective:</h3>
        </div>
        
        <form name = "programs" id = "programs">
            <TextField label = "Objective ID: " value = { id } setValue={setId}/>
            <TextField label = "Objective Code: " value = { code } setValue={setCode}/>
            <TextField label = "Description: " value = { description } setValue={setDescription}/>
            <TextField label = "Department ID:" value = { deptID } setValue={setDeptID}/>
            <button
                type = "button"
                onClick = {() => {
                    handleSubmit()
                }}
            >
                Add Learning Objective
            </button>
        </form>

        {success}
    </>
};