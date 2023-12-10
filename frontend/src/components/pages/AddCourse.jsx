import { useState } from "react";
import { addCourse } from "../../api";
import { TextField } from "../common/TextField";

export const AddCourse = () => {
    const [deptCode, setDeptCode] = useState("");
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [success, setSuccess] = useState("");

    const handleSubmit = () => {
        addCourse({ DeptCode: deptCode, Title: title, Description: description })
            .then(x => {
                setSuccess("Successfully added course.");
            })
            .catch(x => {
                setSuccess("Failed to add course.");
            });
    };

    return (
        <>
            <div>
                <h3>Input Information to Add Course:</h3>
            </div>
            <form id="courses">
                <TextField label="Department Code: " value={deptCode} setValue={setDeptCode} />
                <TextField label="Title: " value={title} setValue={setTitle} />
                <TextField label="Description: " value={description} setValue={setDescription} />
                <button type="button" onClick={handleSubmit}>
                    Add Course
                </button>
            </form>
            <div>{success}</div>
        </>
    );
};

