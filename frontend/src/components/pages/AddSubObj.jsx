import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { addSubObjective } from "../../api";
import { TextField } from "../common/TextField";
import { Department, Faculty, Program, Section, Course, Objective, SubObjective, CourseObjective } from "../../models";

export const AddSubObj = () => {
    const [ subobjectives, setSubObjectives ] = useState([]);
    const [ subObjCode, setSubObjCode ] = useState("");
    const [ description, setDescription ] = useState("");
    const [ objCode, setObjCode ] = useState("");
    const [ success, setSuccess ] = useState("");


    const handleSubmit = () => {
        addSubObjective(new SubObjective(subObjCode, description, objCode)).then(x => {
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
            <TextField label = "Sub-Objective Code: " value = { subObjCode } setValue={setSubObjCode}/>
            <TextField label = "Description: " value = { description } setValue={setDescription}/>
            <TextField label = "Objective Code: " value = { objCode } setValue={setObjCode}/>
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