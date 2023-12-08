import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { addSubObjective } from "../../api";
import { TextField } from "../common/TextField";
import { Department, Faculty, Program, Section, Course, Objective, SubObjective, CourseObjective } from "../../models";

export const AddSubObj = () => {
    const [ subobjectives, setSubObjectives ] = useState([]);
    const [ id, setId ] = useState("");
    const [ code, setCode ] = useState("");
    const [ description, setDescription ] = useState("");
    const [ parent, setParent ] = useState("");
    const [ success, setSuccess ] = useState("");


    const handleSubmit = () => {
        addSubObjective(new SubObjective(id, code, description, parent)).then(x => {
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
            <TextField label = "Sub-Objective ID: " value = { id } setValue={setId}/>
            <TextField label = "Sub-Objective Code: " value = { code } setValue={setCode}/>
            <TextField label = "Description: " value = { description } setValue={setDescription}/>
            <TextField label = "Parent Objective ID: " value = { parent } setValue={setParent}/>
            <button
                type = "button"
                onClick = {() => {
                    handleSubmit()
                }}
            >
                Add Sub-Objective
            </button>
        </form>

        {success}
    </>
};