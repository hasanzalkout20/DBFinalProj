import { useState } from "react";
import { addFaculty } from "../../api";
import { TextField } from "../common/TextField";

export const AddFaculty = () => {
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [deptCode, setDeptCode] = useState("");
    const [position, setPosition] = useState("");
    const [success, setSuccess] = useState("");

    const handleSubmit = () => {
        addFaculty({ Name: name, Email: email, DeptCode: deptCode, Position: position })
            .then(x => {
                setSuccess("Successfully added faculty.");
            })
            .catch(x => {
                setSuccess("Failed to add faculty.");
            });
    };

    return (
        <>
            <div>
                <h3>Input Information to Add Faculty:</h3>
            </div>
            <form id="faculty">
                <TextField label="Name: " value={name} setValue={setName} />
                <TextField label="Email: " value={email} setValue={setEmail} />
                <TextField label="Department Code: " value={deptCode} setValue={setDeptCode} />
                <TextField label="Position: " value={position} setValue={setPosition} />
                <button type="button" onClick={handleSubmit}>
                    Add Faculty
                </button>
            </form>
            <div>{success}</div>
        </>
    );
};

