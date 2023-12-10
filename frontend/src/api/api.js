import axios from "axios";

// define api endpoint in the backend
const baseEndpoint = 'http://localhost:8000';

export const getAllDepartments = () => new Promise((resolve, reject) => {
    // create apiConfig object with a property
    const apiConfig = {
        
    };

    // log endpoint to the console
    console.log(`${ baseEndpoint }/program`);

    // log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a get request 
    axios.get(`${ baseEndpoint }/department`, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});

// getDepartmentPrograms()
// takes a department parameter and returns a Promise
export const getDepartmentPrograms = (department_name) => new Promise((resolve, reject) => {
    // create apiConfig object with a property
    const apiConfig = {
        params: {
            department_name
        }
    };

    // log endpoint to the console
    console.log(`${ baseEndpoint }/program`);

    // log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a get request 
    axios.get(`${ baseEndpoint }/program`, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});

// getDepartmentFaculty() - takes a department parameter and returns a Promise
export const getDepartmentFaculty = (department_name) => new Promise((resolve, reject) => {
    // create apiConfig object with a property
    const apiConfig = {
        params: {
            department_name
        }
    };

    // log endpoint to the console
    console.log(`${ baseEndpoint }/faculty`);

    // log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a get request 
    axios.get(`${ baseEndpoint }/faculty`, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});

// getEvaluation() - takes a department parameter and returns a Promise
export const getEvaluation = (semester, program_name, year) => new Promise((resolve, reject) => {
    // create apiConfig object with a property
    const apiConfig = {
        params: {
            program_name,
            semester,
            year
        }
        
    };

    // log endpoint to the console
    console.log(`${ baseEndpoint }/evaluation_program_semester`);

    // log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a get request 
    axios.get(`${ baseEndpoint }/evaluation_program_semester`, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});

// evaluationYear() - 
export const getEvaluationYear = (year) => new Promise((resolve, reject) => {
    // create apiConfig object with a property
    const apiConfig = {
        params: {
            year
        }
    };

    // log endpoint to the console
    console.log(`${ baseEndpoint }/evaluation_year`);

    // log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a get request 
    axios.get(`${ baseEndpoint }/evaluation_year`, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});

// addDepartment()
export const addDepartment = (department) => new Promise((resolve, reject) => {
    const apiConfig = {

    }

    // for debugging: log endpoint to the console
    console.log(`${ baseEndpoint }/department`);

    // for debugging: log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a post request 
    axios.post(`${ baseEndpoint }/department`, department, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});

// addFaculty()
export const addFaculty = (faculty) => new Promise((resolve, reject) => {
    const apiConfig = {

    }

    // log endpoint to the console
    console.log(`${ baseEndpoint }/faculty`);

    // log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a post request 
    axios.post(`${ baseEndpoint }/faculty`, faculty, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});

// addProgram()
export const addProgram = (program) => new Promise((resolve, reject) => {
    const apiConfig = {

    }

    // for debugging: log endpoint to the console
    console.log(`${ baseEndpoint }/program`);

    // for debugging: log apiConfig object to the console
    console.log(program);

    // use axios to make a post request 
    axios.post(`${ baseEndpoint }/program`, program, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});

//addCourse() - course
export const addCourse = (course) => new Promise((resolve, reject) => {
    const apiConfig = {

    }

    // for debugging: log endpoint to the console
    console.log(`${ baseEndpoint }/course`);

    // for debugging: log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a post request 
    axios.post(`${ baseEndpoint }/course`, course, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});


//addSection()
export const addSection = (section) => new Promise((resolve, reject) => {
    const apiConfig = {

    }

    // for debugging: log endpoint to the console
    console.log(`${ baseEndpoint }/section`);

    // for debugging: log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a post request 
    axios.post(`${ baseEndpoint }/section`, section, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});

//addObjective()
export const addObjective = (objective) => new Promise((resolve, reject) => {
    const apiConfig = {

    }

    // for debugging: log endpoint to the console
    console.log(`${ baseEndpoint }/objective`);

    // for debugging: log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a post request 
    axios.post(`${ baseEndpoint }/objective`, objective, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});

//addSubobjective()
export const addSubObjective = (subobjective) => new Promise((resolve, reject) => {
    const apiConfig = {

    }

    // for debugging: log endpoint to the console
    console.log(`${ baseEndpoint }/subobjective`);

    // for debugging: log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a post request 
    axios.post(`${ baseEndpoint }/subobjective`, subobjective, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});

//def linkCourseToProgram():
export const linkCourseToProgram = (CourseID, ProgID) => new Promise((resolve, reject) => {
    const apiConfig = {


    }

    // for debugging: log endpoint to the console
    console.log(`${ baseEndpoint }/link_course_program`);

    // for debugging: log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a post request 
    axios.post(`${ baseEndpoint }/link_course_program`, { CourseID, ProgID }, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});

export const linkCourseObjective = (CourseID, ProgID, ObjID) => new Promise((resolve, reject) => {
    const apiConfig = {

    }

    // for debugging: log endpoint to the console
    console.log(`${ baseEndpoint }/assign_objective`);

    // for debugging: log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a post request 
    axios.post(`${ baseEndpoint }/assign_objective`, { CourseID, ProgID, ObjID }, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});

//addEvaluationResult()
export const addEvaluationResult = (evaluationresult) => new Promise((resolve, reject) => {
    const apiConfig = {

    }

    // for debugging: log endpoint to the console
    console.log(`${ baseEndpoint }/evaluation`);

    // for debugging: log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a post request 
    axios.post(`${ baseEndpoint }/evaluation`, evaluationresult, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});

// api: program_course_and_objectives()
export const getProgramCoursesObjectives = (program_name) => new Promise((resolve, reject) => {
    // create apiConfig object with a property
    const apiConfig = {
        params: {
            program_name
        }
    };

    // use axios to make a get request 
    axios.get(`${ baseEndpoint }/program_courses_objectives`, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});

// 
export const getProgramObjectives = (department) => new Promise((resolve, reject) => {
    // create apiConfig object with a property
    const apiConfig = {
        params: {
            department
        }
    };

    // use axios to make a get request 
    axios.get(`${ baseEndpoint }/program_courses_objectives`, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});

