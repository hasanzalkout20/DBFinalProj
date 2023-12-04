import axios from "axios";

const baseEndpoint = "http://localhost:8000";

export const getDepartmentPrograms = (department) => new Promise((resolve, reject) => {
    const apiConfig = {
        department
    };
    console.log(`${ baseEndpoint }/programs`);
    console.log(apiConfig);
    axios.get(`${ baseEndpoint }/programs`, apiConfig)
        .then(x => resolve(x.data))
        .catch(x => {
            alert(x);
            reject(x);
        });
});