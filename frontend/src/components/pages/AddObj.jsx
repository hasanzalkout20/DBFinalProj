import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { addObjective, getAllObjectives } from "../../api";
import { TextField } from "../common/TextField";
import { Department, Faculty, Program, Section, Course, Objective, SubObjective, CourseObjective } from "../../models";

export const AddObj = () => {
    const [ objectives, setObjectives ] = useState([]);
    const [ code, setCode ] = useState("");
    const [ description, setDescription ] = useState("");
    const [ programName, setProgramName ] = useState("");
    const [ success, setSuccess ] = useState("");


    const handleSubmit = () => {
        addObjective(new Objective(code, description, programName)).then(x => {
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
            <TextField label = "Objective Code: " value = { code } setValue={setCode}/>
            <TextField label = "Description: " value = { description } setValue={setDescription}/>
            <TextField label = "Program Name:" value = { programName } setValue={setProgramName}/>
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