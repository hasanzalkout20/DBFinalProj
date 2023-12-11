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
            <div>
                <h3>Querying:</h3>

                {/* Department Query Section */}
                <div className="query-block">
                    <div className="query-input">
                        <TextField label="Department Code: " value={departmentCode} setValue={setDepartmentCode} />
                        <button onClick={handleDepartmentSubmit}>Submit</button>
                    </div>
                    <div className="query-results">
                        <h4>Department Results:</h4>
                        <div>
                            <strong>Programs:</strong>
                            <ul>
                                {departmentDetails?.programs?.map((program, index) => (
                                    <li key={index}>
                                        Program Name: {program[0]}
                                        <ul>
                                            <li>Department Code: {program[1]}</li>
                                            <li>Person in Charge: {program[2]}</li>
                                            <li>University ID: {program[3]}</li>
                                            <li>Email: {program[4]}</li>
                                        </ul>
                                    </li>
                                ))}
                            </ul>
                            <strong>Faculty:</strong>
                            <ul>
                                {departmentDetails?.faculty?.map((faculty, index) => (
                                    <li key={index}>
                                        Faculty ID: {faculty[0]}
                                        <ul>
                                            <li>Name: {faculty[1]}</li>
                                            <li>Email: {faculty[2]}</li>
                                            <li>Department: {faculty[3]}</li>
                                            <li>Rank: {faculty[4]}</li>
                                        </ul>
                                    </li>
                                ))}
                            </ul>
                        </div>
                    </div>

                    {/* Program Query Section */}
                    <div className="query-block">
                        <div className="query-input">
                            <TextField label="Program Name: " value={programName} setValue={setProgramName} />
                            <button onClick={handleProgramSubmit}>Submit</button>
                        </div>
                        <div className="query-results">
                            <h4>Program Results:</h4>
                            <div>
                                <strong>Courses:</strong>
                                <ul>
                                    {programDetails?.courses?.map((course, index) => (
                                        <li key={index}>
                                            <div><strong>Course ID:</strong> {course[0]}</div>
                                            <div><strong>Title:</strong> {course[1]}</div>
                                            <div><strong>Description:</strong> {course[2]}</div>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                            <div>
                                <strong>Objectives:</strong>
                                <ul>
                                    {programDetails?.objectives?.map((objective, index) => (
                                        <li key={index}>
                                            <div><strong>Objective Code:</strong> {objective[0]}</div>
                                            <div><strong>Description:</strong> {objective[1]}</div>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                        </div>
                    </div>

                    {/* Semester-Program Query Section */}
                    <div>
                        <TextField label="Semester: " value={semester} setValue={setSemester} />
                        <TextField label="Year: " value={year} setValue={setYear} />
                        <TextField label="Program: " value={programName2} setValue={setProgramName2} />
                        <button onClick={handleSemesterProgramSubmit}>Submit</button>
                        <div>
                            <h4>Evaluation Results for each section:</h4>
                            <ul>
                                {evaluationResults?.evaluation_results?.map((result, index) => (
                                    <li key={index}>
                                        <div><strong>Course Section:</strong> {result[2]}</div>
                                        <div><strong>Method of Evaluation:</strong> {result[3]}</div>
                                        <div><strong>Semester:</strong> {result[4]}</div>
                                        <div><strong>Year:</strong> {result[5]}</div>
                                        <div><strong>Students Passed:</strong> {result[6]}</div>
                                    </li>
                                ))}
                            </ul>
                        </div>
                    </div>

                    {/* Academic Year Query Section */}
                    <div className="query-block">
                        <div className="query-input">
                            <TextField label="Academic year (e.g., 23-24): " value={academicYear} setValue={setAcademicYear} />
                            <button onClick={handleAcademicYearSubmit}>Submit</button>
                        </div>
                        <div className="query-results">
                            <h4>Evaluation Results for each objective/sub-objective:</h4>
                            <div>
                                <strong>Evaluation Results:</strong>
                                <ul>
                                    {academicYearResults?.evaluation_results?.map((result, index) => (
                                        <li key={index}>
                                            <div><strong>Section:</strong> {result[2]}</div>
                                            <div><strong>Evaluation Method:</strong> {result[3]}</div>
                                            <div><strong>Semester:</strong> {result[4]}</div>
                                            <div><strong>Year:</strong> {result[5]}</div>
                                            <div><strong>Students Passed:</strong> {result[6]}</div>
                                            <div><strong>Objective:</strong> {result[7]}</div>
                                            <div><strong>Objective Description:</strong> {result[8]}</div>
                                            <div><strong>Sub-Objective:</strong> {result[9]}</div>
                                            <div><strong>Sub-Objective Description:</strong> {result[10]}</div>
                                            <div><strong>Students Enrolled:</strong> {result[11]}</div>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                            <div>
                                <strong>Aggregate Results:</strong>
                                {academicYearResults?.aggregated_results && (
                                    <ul>
                                        {Object.keys(academicYearResults.aggregated_results).map((key, index) => (
                                            <li key={index}>
                                                <strong>Objective:</strong> {key}
                                                <ul>
                                                    <li><strong>Total students:</strong> {academicYearResults.aggregated_results[key].total_students}</li>
                                                    <li><strong>Passing students:</strong> {academicYearResults.aggregated_results[key].students_passed}</li>
                                                    <li><strong>Pass Percentage:</strong> {academicYearResults.aggregated_results[key].pass_percentage.toFixed(2)}%</li>
                                                </ul>
                                            </li>
                                        ))}
                                    </ul>
                                )}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
};

