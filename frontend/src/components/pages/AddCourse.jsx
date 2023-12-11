import { useState } from "react";
import { addCourse } from "../../api";
import { TextField } from "../common/TextField";
import { useNavigate } from "react-router-dom";

export const AddCourse = () => {
    const [courseID, setCourseID] = useState("");
    const [deptCode, setDeptCode] = useState("");
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [success, setSuccess] = useState("");

    const navigate = useNavigate();

    const handleSubmit = () => {
        addCourse({ CourseID: courseID, DeptCode: deptCode, Title: title, Description: description })
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
                <TextField label="Course ID: " value={courseID} setValue={setCourseID} />
                <TextField label="Department Code: " value={deptCode} setValue={setDeptCode} />
                <TextField label="Title: " value={title} setValue={setTitle} />
                <TextField label="Description: " value={description} setValue={setDescription} />
                <button type="button" onClick={handleSubmit}>
                    Add Course
                </button>
            </form>
            <div>{success}</div>
            <button type="button" onClick={() => navigate("/")}>
                Return Home
            </button>
        </>
    );
};

