import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { addDepartment, addFaculty, addProgram, addCourse, addSection, addObjective, addSubObjective, linkCourseObjective, getDepartmentFaculty, getDepartmentPrograms } from "../../api";
import { TextField } from "../common/TextField";
import { Department, Faculty, Program, Section, Course, Objective, SubObjective, CourseObjective } from "../../models";

export const Results = () => {
    const [ department, setDepartments ] = useState("");
    const [ programs, setPrograms ] = useState([]);

    const navigate = useNavigate();

    const getPrograms = (department) => {
        getDepartmentPrograms(department).then(x => console.log(x));
    }

    // Check form names and id
    return <>

       


        Querying: 

        Given a Department
        List all its programs
        List all its faculty (including what program each faculty is in charge of, if there is one)

        Given a Program
        List all courses, together with the objectives/sub-objctives assocaition with year
        List all the objectives

        Given a semester and a program:
        List all evaluation results for each section (if data for some sections has not been entered, just indicate that the information is not found)
        
        Given an academic year
        List all evaluation results for each objective/sub-objective
            For each obj/sub-obj, list the course/section that are in involved with evaluating them and list the resutl for each course/section
            For each objective/sub-objective, aggregate the result to show that number (and the percentage) of students
    </>


}