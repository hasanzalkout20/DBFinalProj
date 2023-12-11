import { useState } from "react";
import { addDepartment } from "../../api";
import { TextField } from "../common/TextField";
import { useNavigate } from "react-router-dom";

export const AddDept = () => {
    const [name, setName] = useState("");
    const [code, setCode] = useState("");
    const [success, setSuccess] = useState("");

    const navigate = useNavigate();

    const handleSubmit = () => {
        addDepartment({ DeptName: name, DeptCode: code })
            .then(x => {
                setSuccess("Successfully added department.");
            })
            .catch(x => {
                setSuccess("Failed to add department.");
            });
    };

    return (
        <>
            <div>
                <h3>Input Information to Add Department:</h3>
            </div>
            <form id="departments">
                <TextField label="Department Name: " value={name} setValue={setName} />
                <TextField label="Department Code: " value={code} setValue={setCode} />
                <button type="button" onClick={handleSubmit}>
                    Add Department
                </button>
            </form>
            <div>{success}</div>
            <button type="button" onClick={() => navigate("/")}>
                Return Home
            </button>
        </>
    );
};



