import { useState } from "react";
import { addSubObjective } from "../../api";
import { TextField } from "../common/TextField";
import { useNavigate } from "react-router-dom";

export const AddSubObj = () => {
    const [subObjCode, setSubObjCode] = useState("");
    const [description, setDescription] = useState("");
    const [objCode, setObjCode] = useState("");
    const [success, setSuccess] = useState("");

    const handleSubmit = () => {
        addSubObjective({ SubObjCode: subObjCode, Description: description, ObjCode: objCode })
            .then(() => setSuccess("Successfully added sub-objective."))
            .catch(() => setSuccess("Failed to add sub-objective."));
    };

    const navigate = useNavigate();

    return (
        <>
            <div>
                <h3>Input Information to Add Sub-Objective:</h3>
            </div>
            <form id="sub-objective">
                <TextField label="Sub-Objective Code: " value={subObjCode} setValue={setSubObjCode} />
                <TextField label="Description: " value={description} setValue={setDescription} />
                <TextField label="Objective Code: " value={objCode} setValue={setObjCode} />
                <button type="button" onClick={handleSubmit}>Add Sub-Objective</button>
            </form>
            {success}

            <button type="button" onClick={() => navigate("/")}>
                Return Home
            </button>
        </>
    );
};
