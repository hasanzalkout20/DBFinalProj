import { useState } from "react";
// import { useNavigate } from "react-router-dom";
import { getDepartmentPrograms } from "../../api";
import { TextField } from "../common/TextField";

export const Results = () => {
    const [ department, setDepartments ] = useState("");
    const [ programs, setPrograms ] = useState([]);

    const getPrograms = (department) => {
        getDepartmentPrograms(department).then(x => console.log(x));
    }

    return <>
        Hello world

        <form name = "programs" id = "programs">
            <TextField label = "Department:" value = { department } setValue={setDepartments}/>
            <button
                type = "button"
                onClick = {() => {
                    getPrograms(department)
                }}
            >
                Submit
            </button>
        </form>

        <ul>
            {
                programs.map((program, index) => {
                    return <li key = { index }>{ program }</li>
                })
            }
        </ul>
    </>
}