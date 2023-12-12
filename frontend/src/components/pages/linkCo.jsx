import { useState } from "react";
import { linkCourseObjective } from "../../api";
import { TextField } from "../common/TextField";
import { useNavigate } from "react-router-dom";

export const LinkCo = () => {
    const [CourseObjID, setCourseObjID] = useState(""); 
    const [courseId, setCourseId] = useState("");
    const [objCode, setObjCode] = useState("");
    const [subObjCode, setSubObjCode] = useState("");
    const [success, setSuccess] = useState("");

    const handleSubmit = () => { 
        linkCourseObjective(CourseObjID, courseId, objCode, subObjCode)
            .then(() => setSuccess("Successfully linked course to objective."))
            .catch(() => setSuccess("Failed to link course to objective."));
    }    
    
    const navigate = useNavigate();

    return (
        <>
            <div><h3>Link Course to Objective:</h3></div>
            <form>
                <TextField label="Course Objective ID: " value={CourseObjID} setValue={setCourseObjID}/>
                <TextField label="Course ID: " value={courseId} setValue={setCourseId}/>
                <TextField label="Objective Code: " value={objCode} setValue={setObjCode}/>
                <TextField label="Sub-Objective Code: " value={subObjCode} setValue={setSubObjCode}/>
                <button type="button" onClick={handleSubmit}>Link!</button>
            </form>
            {success}

            <button type="button" onClick={() => navigate("/")}>
                Return Home
            </button>
        </>
    );
};
