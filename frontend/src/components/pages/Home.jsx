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
    const [programName2, setProgramName2] = useState("");
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
        getEvaluationResultsBySemesterAndProgram(semester, year, programName2).then(data => {
            setEvaluationResults(data);
        });
    }

    const handleAcademicYearSubmit = () => {
        let input = academicYear.split("-");
        input = input.map(x => "20" + x);
        getEvaluationResultsByAcademicYear(input[0], input[1]).then(data => {
            setAcademicYearResults(data);
        });
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
                <button onClick={() => navigate("/link/objective")}>Assign a Learning (sub)Objective to a Course</button>
            </div>

            {/* Querying Section */}
            {/* Querying Section */}
            <div><h3>Querying:</h3></div>

            <div>
                <TextField label="Department Code: " value={departmentCode} setValue={setDepartmentCode} />
                <button onClick={handleDepartmentSubmit}>Submit</button>
                <div>
                    <h4>Department Results:</h4>
                    Programs: 
                    <ul>
                        {departmentDetails?.programs?.map((item, i) => <li key={i}>
                            {item[0]}
                            <ul>
                                <li>{item[1]}</li>
                                <li>{item[2]}</li>
                                <li>{item[3]}</li>
                                <li>{item[4]}</li>
                            </ul>
                        </li>)}
                    </ul>
                    Faculty: 
                    <ul>
                        {departmentDetails?.faculty?.map((item, i) => <li key={i}>
                            Faculty ID: {item[0]}
                            <ul>
                                <li>{item[1]}</li>
                                <li>{item[2]}</li>
                                <li>{item[3]}</li>
                                <li>{item[4]}</li>
                            </ul>
                        </li>)}
                    </ul>
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
                <TextField label="Program: " value={programName2} setValue={setProgramName2} />
                <button onClick={handleSemesterProgramSubmit}>Submit</button>
                <div>
                    <h4>Evaluation Results for each section:</h4>
                    Evaluations: <ul>{evaluationResults?.evaluation_results?.map((item, i) => <li key={i}>{item}</li>)}</ul>
                </div>
            </div>

            <div>
                <TextField label="Academic year (e.g., 23-24): " value={academicYear} setValue={setAcademicYear} />
                <button onClick={handleAcademicYearSubmit}>Submit</button>
                <div>
                    <h4>Evaluation Results for each objective/sub-objective:</h4>
                    Evaluation Results: <ul>{academicYearResults?.evaluation_results?.map((item, i) => <li key={i}>{item}</li>)}</ul>
                    Aggregate Results: 
                    {
                        academicYearResults?.aggregated_results && <ul>
                            {
                                Object.keys(academicYearResults.aggregated_results).map((x, i) => <li key = {i}>
                                    {x}
                                    <ul>
                                        <li>Total students: { academicYearResults.aggregated_results[x].total_students }</li>
                                        <li>Passing students: { academicYearResults.aggregated_results[x].students_passed }</li>
                                        <li>Pass Percentage: { academicYearResults.aggregated_results[x].pass_percentage.toFixed(2) }</li>
                                    </ul>
                                </li>)
                            }
                        </ul>
                    }
                </div>
            </div>
        </>
    );
};

