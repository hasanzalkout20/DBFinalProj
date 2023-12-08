import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { addCourse, getAllCourses } from "../../api";  //??
import { TextField } from "../common/TextField";
import { Department, Faculty, Program, Section, Course, Objective, SubObjective, CourseObjective } from "../../models";

export const AddCourse = () => {
    const [ courses, setCourses ] = useState([]);
    const [ id, setId ] = useState("");
    const [ deptID, setDeptID ] = useState("");
    const [ title, setTitle ] = useState("");
    const [ description, setDescription] = useState("");
    const [ success, setSuccess ] = useState("");

    const handleSubmit = () => {
        addCourse(new Course(id, deptID, title, description)).then(x => {
            // getAllDepartments().then(x => setDepartments(x));
            setSuccess("Successfully added");
        }).catch(x => {
            setSuccess("");
        })
    }



    return <>
        <div>
            <h3>Input Information to Add Course:</h3>
        </div>
        
        <form name = "programs" id = "programs">
            <TextField label = "Course ID: " value = { id } setValue={setId}/>
            <TextField label = "Department ID: " value = { deptID } setValue={setDeptID}/>
            <TextField label = "Title: " value = { title } setValue={setTitle}/>
            <TextField label = "Description: " value = { description } setValue={setDescription}/>
            <button
                type = "button"
                onClick = {() => {
                    handleSubmit()
                }}
            >
                Add Course
            </button>
        </form>

        {/* <ul>
            {
                courses.map((course, index) => {
                    return <li key = { index }>{ course[0] }
                        <ul>
                            <li>{ course[1] }</li>
                            <li>{ course[2] }</li>
                            <li>{ course[3] }</li>
                        </ul>
                    </li>
                })
            }
        </ul> */}


        { success }
    </>
};
