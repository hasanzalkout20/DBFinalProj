import { useState } from "react";
import { addObjective } from "../../api";
import { TextField } from "../common/TextField";

export const AddObj = () => {
    const [code, setCode] = useState("");
    const [description, setDescription] = useState("");
    const [programName, setProgramName] = useState("");
    const [success, setSuccess] = useState("");

    const handleSubmit = () => {
        addObjective({ ObjCode: code, Description: description, ProgramName: programName })
            .then(x => {
                setSuccess("Successfully added objective.");
            })
            .catch(x => {
                setSuccess("Failed to add objective.");
            });
    };

    return (
        <>
            <div>
                <h3>Input Information to Add Objective:</h3>
            </div>
            <form id="objectives">
                <TextField label="Objective Code: " value={code} setValue={setCode} />
                <TextField label="Description: " value={description} setValue={setDescription} />
                <TextField label="Program Name: " value={programName} setValue={setProgramName} />
                <button type="button" onClick={handleSubmit}>
                    Add Learning Objective
                </button>
            </form>
            <div>{success}</div>
        </>
    );
};
