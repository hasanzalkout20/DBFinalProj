import { useState } from "react";
import { addFaculty } from "../../api";
import { TextField } from "../common/TextField";
import { useNavigate } from "react-router-dom";

export const AddFaculty = () => {
    const [facultyID, setFacultyID] = useState("");
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [deptCode, setDeptCode] = useState("");
    const [position, setPosition] = useState("");
    const [success, setSuccess] = useState("");

    const handleSubmit = () => {
        addFaculty({ FacultyID: facultyID, Name: name, Email: email, DeptCode: deptCode, Position: position })
            .then(x => {
                setSuccess("Successfully added faculty.");
            })
            .catch(x => {
                setSuccess("Failed to add faculty.");
            });
    };

    const navigate = useNavigate();

    return (
        <>
            <div>
                <h3>Input Information to Add Faculty:</h3>
            </div>
            <form id="faculty">
                <TextField label="Faculty ID: " value={facultyID} setValue={setFacultyID} />
                <TextField label="Name: " value={name} setValue={setName} />
                <TextField label="Email: " value={email} setValue={setEmail} />
                <TextField label="Department Code: " value={deptCode} setValue={setDeptCode} />
                <TextField label="Position: " value={position} setValue={setPosition} />
                <button type="button" onClick={handleSubmit}>
                    Add Faculty
                </button>
            </form>
            <div>{success}</div>

            <button type="button" onClick={() => navigate("/")}>
                Return Home
            </button>
        </>
    );
};

