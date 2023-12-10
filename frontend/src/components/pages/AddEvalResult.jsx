import { useState } from "react";
import { addEvaluationResult } from "../../api";
import { TextField } from "../common/TextField";

export const AddEvalResult = () => {
    const [courseObjID, setCourseObjID] = useState("");
    const [sectionID, setSectionID] = useState("");
    const [evalMethod, setEvalMethod] = useState("");
    const [semester, setSemester] = useState("");
    const [year, setYear] = useState("");
    const [studentsPassed, setStudentsPassed] = useState("");
    const [success, setSuccess] = useState("");

    const handleSubmit = () => {
        addEvaluationResult({ CourseObjID: courseObjID, SectionID: sectionID, EvalMethod: evalMethod, Semester: semester, Year: year, StudentsPassed: studentsPassed })
            .then(() => setSuccess("Successfully added evaluation result."))
            .catch(() => setSuccess("Failed to add evaluation result."));
    };

    return (
        <>
            <div>
                <h3>Input Information to Add Evaluation Result:</h3>
            </div>
            <form id="evaluation-result">
                <TextField label="Course Objective ID: " value={courseObjID} setValue={setCourseObjID} />
                <TextField label="Section ID: " value={sectionID} setValue={setSectionID} />
                <TextField label="Evaluation Method: " value={evalMethod} setValue={setEvalMethod} />
                <TextField label="Semester: " value={semester} setValue={setSemester} />
                <TextField label="Year: " value={year} setValue={setYear} />
                <TextField label="Number of Students Passed: " value={studentsPassed} setValue={setStudentsPassed} />
                <button type="button" onClick={handleSubmit}>Add Evaluation Result</button>
            </form>
            {success}
        </>
    );
};



