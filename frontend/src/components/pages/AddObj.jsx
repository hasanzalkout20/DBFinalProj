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
    const [ deptId, setDeptID ] = useState("");


    const handleSubmit = () => {
        addObjective(new Objective(id, code, description, deptID)).then(x => {
            getAllObjectives().then(x => setObjectives(x));
        })
    }

    useEffect(() => {
        getAllObjectives().then(x => setObjectives(x));
    }, []);

    useEffect(() => {
        console.log(objectives)
    }, [objectives])

    return <>
        <div>
            <h3>Input Information to Add Objective:</h3>
        </div>
        
        <form name = "programs" id = "programs">
            <TextField label = "Objective ID: " value = { id } setValue={setId}/>
            <TextField label = "Objective Code: " value = { code } setValue={setCode}/>
            <TextField label = "Description: " value = { description } setValue={setDescription}/>
            <TextField label = "Department ID:" value = { deptId } setValue={setDeptID}/>
            <button
                type = "button"
                onClick = {() => {
                    getAllObjectives(Objective)
                }}
            >
                Add Learning Objective
            </button>
        </form>

        <ul>
            {
                objectives.map((objective, index) => {
                    return <li key = { index }>{ objective[0] }
                        <ul>
                            <li>{ objective[1] }</li>
                            <li>{ objective[2] }</li>
                            <li>{ objective[3] }</li>
                        </ul>
                    </li>
                })
            }
        </ul>
    </>
};