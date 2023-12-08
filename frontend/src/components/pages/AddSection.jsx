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


    const handleSubmit = () => {
        addSection(new Section(secId, courseID, semester, year, facultyLeadID, enrollCount)).then(x => {
            getAllSections().then(x => setSections(x));  
        })
    }

    useEffect(() => {
        getAllSections().then(x => setSections(x)); 
    }, []);

    useEffect(() => {
        console.log(sections)
    }, [sections])

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
                    getAllSections(Section)
                }}
            >
                Add Section
            </button>
        </form>

        <ul>
            {
                sections.map((section, index) => {
                    return <li key = { index }>{ section[0] }
                        <ul>
                            <li>{ section[1] }</li>
                            <li>{ section[2] }</li>
                            <li>{ section[3] }</li>
                            <li>{ section[4] }</li>
                            <li>{ section[5] }</li>
                        </ul>
                    </li>
                })
            }
        </ul>
    </>
};