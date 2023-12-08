import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { addSection, getAllSections } from "../../api"; 
import { TextField } from "../common/TextField";
import { Department, Faculty, Program, Section, Course, Objective, SubObjective, CourseObjective } from "../../models";

export const AddSection = () => {
    const [ sections, setSections ] = useState([]);
    const [ secId, setSecId ] = useState("");
    const [ courseID, setCourseID ] = useState("");
    const [ semester, setSemester ] = useState("");
    const [ year, setYear ] = useState("");
    const [ facultyLeadID, setFacultyLeadID ] = useState("");
    const [ enrollCount, setEnrollCount ] = useState("");
    const [ success, setSuccess ] = useState("");


    const handleSubmit = () => {
        addSection(new Section(secId, courseID, semester, year, facultyLeadID, enrollCount)).then(x => {
            // getAllDepartments().then(x => setDepartments(x));
            setSuccess("Successfully added");
        }).catch(x => {
            setSuccess("");
        })
    }

  

    return <>
        <div>
            <h3>Input Information to Add Section:</h3>
        </div>
        
        <form name = "programs" id = "programs">
            <TextField label = "Section ID: " value = { secId } setValue={setSecId}/>            
            <TextField label = "Course ID: " value = { courseID } setValue={setCourseID}/>
            <TextField label = "Semester: " value = { semester } setValue={setSemester}/>
            <TextField label = "Year: " value = { year } setValue={setYear}/>
            <TextField label = "Faculty Lead ID: " value = { facultyLeadID } setValue={setFacultyLeadID}/>
            <TextField label = "Enrollment Count: " value = { enrollCount } setValue={setEnrollCount}/>
            <button
                type = "button"
                onClick = {() => {
                    handleSubmit()
                }}
            >
                Add Section
            </button>
        </form>

        {success}
    </>
};