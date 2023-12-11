import { useState } from "react";
import { addSection } from "../../api";
import { TextField } from "../common/TextField";
import { useNavigate } from "react-router-dom";

export const AddSection = () => {
    const [sectionId, setSectionId] = useState("");
    const [courseID, setCourseID] = useState("");
    const [semester, setSemester] = useState("");
    const [year, setYear] = useState("");
    const [facultyLeadID, setFacultyLeadID] = useState("");
    const [enrollCount, setEnrollCount] = useState("");
    const [success, setSuccess] = useState("");

    const handleSubmit = () => {
        addSection({ SectionID: sectionId, CourseID: courseID, Semester: semester, Year: year, FacultyLeadID: facultyLeadID, EnrollCount: enrollCount })
            .then(() => setSuccess("Successfully added section."))
            .catch(() => setSuccess("Failed to add section."));
    };

    const navigate = useNavigate();

    return (
        <>
            <div>
                <h3>Input Information to Add Section:</h3>
            </div>
            <form id="section">
                <TextField label="Section ID: " value={sectionId} setValue={setSectionId} />
                <TextField label="Course ID: " value={courseID} setValue={setCourseID} />
                <TextField label="Semester: " value={semester} setValue={setSemester} />
                <TextField label="Year: " value={year} setValue={setYear} />
                <TextField label="Faculty Lead ID: " value={facultyLeadID} setValue={setFacultyLeadID} />
                <TextField label="Enrollment Count: " value={enrollCount} setValue={setEnrollCount} />
                <button type="button" onClick={handleSubmit}>Add Section</button>
            </form>
            {success}

            <button type="button" onClick={() => navigate("/")}>
                Return Home
            </button>
        </>
    );
};
