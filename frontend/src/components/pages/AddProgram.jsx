import { useState } from "react";
import { addProgram } from "../../api";
import { TextField } from "../common/TextField";

export const AddProgram = () => {
    const [name, setName] = useState("");
    const [deptCode, setDeptCode] = useState("");
    const [facultyLeadName, setFacultyLeadName] = useState("");
    const [facultyLeadID, setFacultyLeadID] = useState("");
    const [facultyLeadEmail, setFacultyLeadEmail] = useState("");
    const [success, setSuccess] = useState("");

    const handleSubmit = () => {
        addProgram({ ProgramName: name, DeptCode: deptCode, FacultyLeadName: facultyLeadName, FacultyLeadID: facultyLeadID, FacultyLeadEmail: facultyLeadEmail })
            .then(() => setSuccess("Successfully added program."))
            .catch(() => setSuccess("Failed to add program."));
    };

    return (
        <>
            <div>
                <h3>Input Information to Add Program:</h3>
            </div>
            <form id="program">
                <TextField label="Program Name: " value={name} setValue={setName} />
                <TextField label="Department Code: " value={deptCode} setValue={setDeptCode} />
                <TextField label="Faculty Lead Name: " value={facultyLeadName} setValue={setFacultyLeadName} />
                <TextField label="Faculty Lead ID: " value={facultyLeadID} setValue={setFacultyLeadID} />
                <TextField label="Faculty Lead Email: " value={facultyLeadEmail} setValue={setFacultyLeadEmail} />
                <button type="button" onClick={handleSubmit}>Add Program</button>
            </form>
            {success}
        </>
    );
};

