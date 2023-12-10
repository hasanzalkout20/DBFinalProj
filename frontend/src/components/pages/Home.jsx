import { useState } from "react";
import { useNavigate } from "react-router-dom";
import {
    getDepartmentDetails, getProgramCoursesObjectives,
    getEvaluationResultsBySemesterAndProgram, getEvaluationResultsByAcademicYear
} from "../../api";
import { TextField } from "../common/TextField";

export const Home = () => {
    const [departmentCode, setDepartmentCode] = useState("");
    const [programName, setProgramName] = useState("");
    const [semester, setSemester] = useState("");
    const [year, setYear] = useState("");
    const [academicYear, setAcademicYear] = useState("");
    const [departmentDetails, setDepartmentDetails] = useState(null);
    const [programDetails, setProgramDetails] = useState(null);
    const [evaluationResults, setEvaluationResults] = useState([]);
    const [academicYearResults, setAcademicYearResults] = useState([]);

    const navigate = useNavigate();

    const handleDepartmentSubmit = () => {
        getDepartmentDetails(departmentCode).then(data => {
            setDepartmentDetails(data);
        });
    };

    const handleProgramSubmit = () => {
        getProgramCoursesObjectives(programName).then(data => {
            setProgramDetails(data);
        });
    };

    const handleSemesterProgramSubmit = () => {
        getEvaluationResultsBySemesterAndProgram(semester, year, programName).then(setEvaluationResults);
    }

    const handleAcademicYearSubmit = () => {
        getEvaluationResultsByAcademicYear(academicYear).then(setAcademicYearResults);
    }

    return (
        <>
            {/* Data Entry Section */}
            <div><h3>Add Data:</h3></div>
            <div>
                <button onClick={() => navigate("/add/department")}>Add Department</button>
                <button onClick={() => navigate("/add/faculty")}>Add Faculty</button>
                <button onClick={() => navigate("/add/program")}>Add Program</button>
                <button onClick={() => navigate("/add/course")}>Add Course</button>
                <button onClick={() => navigate("/add/section")}>Add Section</button>
                <button onClick={() => navigate("/add/objective")}>Add Objective</button>
                <button onClick={() => navigate("/add/sub_objective")}>Add Sub-Objective</button>
                <button onClick={() => navigate("/add/evaluation")}>Add Evaluation Results</button>
                <button onClick={() => navigate("/link/program")}>Assign a Course to a Program</button>
                <button onClick={() => navigate("/link/objective")}>Assign a Learning Objective to a Course</button>
            </div>

            {/* Querying Section */}
            {/* Querying Section */}
            <div><h3>Querying:</h3></div>

            <div>
                <TextField label="Department Code: " value={departmentCode} setValue={setDepartmentCode} />
                <button onClick={handleDepartmentSubmit}>Submit</button>
                <div>
                    <h4>Department Results:</h4>
                    Programs: <ul>{departmentDetails?.programs?.map((item, i) => <li key={i}>{item}</li>)}</ul>
                    Faculty: <ul>{departmentDetails?.faculty?.map((item, i) => <li key={i}>{item}</li>)}</ul>
                </div>
            </div>

            <div>
                <TextField label="Program Name: " value={programName} setValue={setProgramName} />
                <button onClick={handleProgramSubmit}>Submit</button>
                <div>
                    <h4>Program Results:</h4>
                    Courses: <ul>{programDetails?.courses?.map((item, i) => <li key={i}>{item}</li>)}</ul>
                    Objectives: <ul>{programDetails?.objectives?.map((item, i) => <li key={i}>{item}</li>)}</ul>
                </div>
            </div>

            <div>
                <TextField label="Semester: " value={semester} setValue={setSemester} />
                <TextField label="Year: " value={year} setValue={setYear} />
                <TextField label="Program: " value={programName} setValue={setProgramName} />
                <button onClick={handleSemesterProgramSubmit}>Submit</button>
                <div>
                    <h4>Evaluation Results for each section:</h4>
                    Evaluations: <ul>{evaluationResults.map((item, i) => <li key={i}>{item}</li>)}</ul>
                </div>
            </div>

            <div>
                <TextField label="Academic year (e.g., 23-24): " value={academicYear} setValue={setAcademicYear} />
                <button onClick={handleAcademicYearSubmit}>Submit</button>
                <div>
                    <h4>Evaluation Results for each objective/sub-objective:</h4>
                    Evaluations: <ul>{academicYearResults.map((item, i) => <li key={i}>{item}</li>)}</ul>
                </div>
            </div>
        </>
    );
};

