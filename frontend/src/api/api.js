import axios from "axios";

// define api endpoint in the backend
const baseEndpoint = "http://localhost:8000";

export const getAllDepartments = () => new Promise((resolve, reject) => {
    // create apiConfig object with a property
    const apiConfig = {
        
    };

    // log endpoint to the console
    console.log(`${ baseEndpoint }/programs`);

    // log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a get request 
    axios.get(`${ baseEndpoint }/departments`, apiConfig)
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
export const getDepartmentPrograms = (department) => new Promise((resolve, reject) => {
    // create apiConfig object with a property
    const apiConfig = {
        department
    };

    // log endpoint to the console
    console.log(`${ baseEndpoint }/programs`);

    // log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a get request 
    axios.get(`${ baseEndpoint }/programs`, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});

// getDepartmentFaculty() - takes a department parameter and returns a Promise
export const getDepartmentFaculty = (department) => new Promise((resolve, reject) => {
    // create apiConfig object with a property
    const apiConfig = {
        department
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
export const getEvaluation = (department) => new Promise((resolve, reject) => {
    // create apiConfig object with a property
    const apiConfig = {
        department
    };

    // log endpoint to the console
    console.log(`${ baseEndpoint }/evaluation`);

    // log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a get request 
    axios.get(`${ baseEndpoint }/evaluation`, apiConfig)
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
    console.log(apiConfig);

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

//linkCourseObjective():
export const linkCourseObjective = (courseobjective) => new Promise((resolve, reject) => {
    const apiConfig = {

    }

    // for debugging: log endpoint to the console
    console.log(`${ baseEndpoint }/courseobjective`);

    // for debugging: log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a post request 
    axios.post(`${ baseEndpoint }/courseobjective`, courseobjective, apiConfig)
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
    console.log(`${ baseEndpoint }/evaluationresult`);

    // for debugging: log apiConfig object to the console
    console.log(apiConfig);

    // use axios to make a post request 
    axios.post(`${ baseEndpoint }/evaluationresult`, evaluationresult, apiConfig)
        // if request is success, resolve Promise iwth data received from request
        .then(x => resolve(x.data))

        // if there is an error, alerts the error and rejects the Promise with the error object received 
        .catch(x => {
            alert(x);
            reject(x);
        });
});

