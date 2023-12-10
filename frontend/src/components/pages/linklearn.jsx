import { useState, useEffect } from "react";
import { linkCourseToProgram } from "../../api";
import { TextField } from "../common/TextField";

export const LinkLearn = () => {
    const [courseId, setCourseId] = useState("");
    const [progId, setProgId] = useState("");
    const [success, setSuccess] = useState("");

    const handleSubmit = () => {
        linkCourseToProgram({ courseId, progId }).then(() => {
            setSuccess("Successfully linked course to program.");
        }).catch(() => {
            setSuccess("Failed to link course to program.");
        });
    };

    return (
        <>
            <div><h3>Link Course to Program:</h3></div>
            <form>
                <TextField label="Course ID: " value={courseId} setValue={setCourseId}/>
                <TextField label="Program ID: " value={progId} setValue={setProgId}/>
                <button type="button" onClick={handleSubmit}>Link!</button>
            </form>
            {success}
        </>
    );
};
