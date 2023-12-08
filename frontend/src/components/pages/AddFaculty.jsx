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
    const [ deptID, setDeptId ] = useState("");
    const [ position, setPosition ] = useState("");
    

    const handleSubmit = () => {
        addFaculty(new Faculty(id, name, email, deptID, position)).then(x => {
            getDepartmentFaculty().then(x => setFaculty(x));
        })
    }

    useEffect(() => {
        getDepartmentFaculty().then(x => setFaculty(x));
    }, []);

    useEffect(() => {
        console.log(faculty)
    }, [faculty])

    return <>
        <div>
            <h3>Input Information to Add Faculty:</h3>
        </div>
        
        <form name = "faculty" id = "faculty">
            <TextField label = "Faculty ID: " value = { id } setValue={setId}/>
            <TextField label = "Name: " value = { name } setValue={setName}/>
            <TextField label = "Email: " value = { email } setValue={setEmail}/>
            <TextField label = "Department ID: " value = { deptID } setValue={setDeptId}/>
            <TextField label = "Position: " value = { position } setValue={setPosition}/>
            <button
                type = "button"
                onClick = {() => {
                    getDepartmentFaculty(Faculty)
                }}
            >
                Add Faculty
            </button>
        </form>

        <ul>
            {
                faculty.map((faculty, index) => {
                    return <li key = { index }>{ faculty[0] }
                        <ul>
                            <li>{ department[1] }</li>
                            <li>{ department[2] }</li>
                            <li>{ department[3] }</li>
                            <li>{ department[4] }</li>
                            
                        </ul>
                    </li>
                })
            }
        </ul>
    </>
};
