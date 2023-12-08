import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { addDepartment, getAllDepartments } from "../../api";
import { TextField } from "../common/TextField";
import { Department, Faculty, Program, Section, Course, Objective, SubObjective, CourseObjective } from "../../models";

export const AddDept = () => {
    const [ departments, setDepartments ] = useState([]);
    const [ id, setId ] = useState("");
    const [ name, setName ] = useState("");
    const [ code, setCode ] = useState("");

    const handleSubmit = () => {
        addDepartment(new Department(id, name, code)).then(x => {
            getAllDepartments().then(x => setDepartments(x));
        })
    }

    useEffect(() => {
        getAllDepartments().then(x => setDepartments(x));
    }, []);

    useEffect(() => {
        console.log(departments)
    }, [departments])

    return <>
        <div>
            <h3>Input Information to Add Department:</h3>
        </div>
        
        <form name = "programs" id = "programs">
            <TextField label = "Department ID: " value = { id } setValue={setId}/>
            <TextField label = "Department Name: " value = { name } setValue={setName}/>
            <TextField label = "Department Code: " value = { code } setValue={setCode}/>
            <button
                type = "button"
                onClick = {() => handleSubmit()}
            >
                Add Department
            </button>
        </form>

        <ul>
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
        </ul>
    </>
};


