import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { addSubObjective, getAllSubObjectives } from "../../api";
import { TextField } from "../common/TextField";
import { Department, Faculty, Program, Section, Course, Objective, SubObjective, CourseObjective } from "../../models";

export const AddObj = () => {
    const [ subobjectives, setSubObjectives ] = useState([]);
    const [ id, setId ] = useState("");
    const [ code, setCode ] = useState("");
    const [ description, setDescription ] = useState("");
    const [ parent, setParent ] = useState("");


    const handleSubmit = () => {
        addSubObjective(new SubObjective(id, code, description, parent)).then(x => {
            getAllSubObjectives().then(x => setSubObjectives(x));
        })
    }

    useEffect(() => {
        getAllObjectives().then(x => setSubObjectives(x));
    }, []);

    useEffect(() => {
        console.log(subobjectives)
    }, [subobjectives])

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
                    getAllSubObjectives(SubObjective)
                }}
            >
                Add Sub-Objective
            </button>
        </form>

        <ul>
            {
                subobjectives.map((subobjective, index) => {
                    return <li key = { index }>{ subobjective[0] }
                        <ul>
                            <li>{ subobjective[1] }</li>
                            <li>{ subobjective[2] }</li>
                            <li>{ subobjective[3] }</li>
                        </ul>
                    </li>
                })
            }
        </ul>
    </>
};