import { useState } from "react";
import { linkCourseObjective } from "../../api";
import { TextField } from "../common/TextField";
import { useNavigate } from "react-router-dom";

export const LinkCo = () => {
    const [courseId, setCourseId] = useState("");
    const [progId, setProgId] = useState("");
    const [objId, setObjId] = useState("");
    const [success, setSuccess] = useState("");

    const handleSubmit = () => {
        linkCourseObjective({ courseId, progId, objId }).then(() => {
            setSuccess("Successfully linked course to objective.");
        }).catch(() => {
            setSuccess("Failed to link course to objective.");
        });
    };

    const navigate = useNavigate();

    return (
        <>
            <div><h3>Link Course to Objective:</h3></div>
            <form>
                <TextField label="Course ID: " value={courseId} setValue={setCourseId}/>
                <TextField label="Program ID: " value={progId} setValue={setProgId}/>
                <TextField label="Objective ID: " value={objId} setValue={setObjId}/>
                <button type="button" onClick={handleSubmit}>Link!</button>
            </form>
            {success}

            <button type="button" onClick={() => navigate("/")}>
                Return Home
            </button>
        </>
    );
};
