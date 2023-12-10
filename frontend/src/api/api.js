import axios from "axios";

// Base endpoint for backend API
const baseEndpoint = 'http://localhost:8000';

const apiConfig = {
    headers: { 'Content-Type': 'application/json' }
};

// Helper functions for API requests
const makeGetRequest = async (path, params) => {
    try {
        const response = await axios.get(`${baseEndpoint}${path}`, { ...apiConfig, params });
        return response.data;
    } catch (error) {
        console.error('Error making GET request:', error);
        throw error;
    }
};

const makePostRequest = async (path, data) => {
    try {
        const response = await axios.post(`${baseEndpoint}${path}`, data, apiConfig);
        return response.data;
    } catch (error) {
        console.error('Error making POST request:', error);
        throw error;
    }
};

// API functions
export const getDepartmentDetails = (deptCode) => makeGetRequest('/department/details', { deptCode });
export const getProgramCoursesObjectives = (programName) => makeGetRequest('/program/courses_objectives', { programName });
export const getEvaluationResultsBySemesterAndProgram = (semester, year, programName) => makeGetRequest('/program/evaluation_results', { semester, year, programName });
export const getEvaluationResultsByAcademicYear = (startYear, endYear) => makeGetRequest('/objectives/evaluation_results', { startYear, endYear });

export const addDepartment = (department) => makePostRequest('/department', department);
export const addFaculty = (faculty) => makePostRequest('/faculty', faculty);
export const addProgram = (program) => makePostRequest('/program', program);
export const addCourse = (course) => makePostRequest('/course', course);
export const addSection = (section) => makePostRequest('/section', section);
export const addObjective = (objective) => makePostRequest('/objective', objective);
export const addSubObjective = (subobjective) => makePostRequest('/subobjective', subobjective);
export const linkCourseToProgram = (CourseID, ProgID) => makePostRequest('/courseobjective', { CourseID, ProgID });
export const linkCourseObjective = (CourseID, ProgID, ObjID) => makePostRequest('/assign_objective', { CourseID, ProgID, ObjID });
export const addEvaluationResult = (evaluationresult) => makePostRequest('/evaluation', evaluationresult);


