import { useState } from "react";
// import { useNavigate } from "react-router-dom";
import { addDepartment, addFaculty, addProgram, addCourse, addSection, addObjective, addSubObjective, linkCourseObjective, getDepartmentFaculty, getDepartmentPrograms } from "../../api";
import { TextField } from "../common/TextField";
import { Department, Faculty, Program, Section, Course, Objective, SubObjective, CourseObjective } from "../../models";

export const Results = () => {
    const [ department, setDepartments ] = useState("");
    const [ programs, setPrograms ] = useState([]);

    const getPrograms = (department) => {
        getDepartmentPrograms(department).then(x => console.log(x));
    }

    return <>

        <div>
            <h3>Input Data About Departments:</h3>
        </div>
        
        <form name = "programs" id = "programs">
            <TextField label = "Department ID: " value = { department } setValue={addDepartment}/>
            <TextField label = "Department Name: " value = { department } setValue={addDepartment}/>
            <TextField label = "Department Code: " value = { department } setValue={addDepartment}/>
            <button
                type = "button"
                onClick = {() => {
                    getPrograms(department)
                }}
            >
                Update Department Information
            </button>
        </form>

        <ul>
            {
                programs.map((program, index) => {
                    return <li key = { index }>{ program }</li>
                })
            }
        </ul>

        <div>
            <h3>Input Data About Faculty:</h3>
        </div>
       

        <form name = "faculty" id = "faculty">
            <TextField label = "Faculty ID: " value = { Faculty } setValue={addFaculty}/>
            <TextField label = "Name: " value = { Faculty } setValue={addFaculty}/>
            <TextField label = "Email: " value = { Faculty } setValue={addFaculty}/>
            <TextField label = "Department ID: " value = { Faculty } setValue={addFaculty}/>
            <TextField label = "Position: " value = { Faculty } setValue={addFaculty}/>
            <button
                type = "button"
                onClick = {() => {
                    getDepartmentFaculty(Faculty)
                }}
            >
                Update Faculty Information
            </button>
        </form>

        <ul>
            {
                programs.map((program, index) => {
                    return <li key = { index }>{ program }</li>
                })
            }
        </ul>

        <div>
            <h3>Input Data About Programs:</h3>
        </div>

        <form name = "programs" id = "programs">
            <TextField label = "Program ID: " value = { programs } setValue={addProgram}/>
            <TextField label = "Program Name: " value = { programs } setValue={addProgram}/>
            <TextField label = "Department ID: " value = { programs } setValue={addProgram}/>
            <TextField label = "Faculty Lead ID: " value = { programs } setValue={addProgram}/>
            <TextField label = "Faculty Lead Email: " value = { programs } setValue={addProgram}/>
            <button
                type = "button"
                onClick = {() => {
                    getPrograms(Program)
                }}
            >
                Update Program Information
            </button>
        </form>

        <ul>
            {
                programs.map((program, index) => {
                    return <li key = { index }>{ program }</li>
                })
            }
        </ul>


        <div>
            <h3>Input Data About Courses:</h3>
        </div>

        <form name = "course" id = "courses">
            <TextField label = "Course ID: " value = { Course } setValue={addCourse}/>
            <TextField label = "Department ID: " value = { Course } setValue={addCourse}/>
            <TextField label = "Title: " value = { Course } setValue={addCourse}/>
            <TextField label = "Description: " value = { Course } setValue={addCourse}/>
            <button
                type = "button"
                onClick = {() => {
                    getPrograms(Course)
                }}
            >
                Update Course Information
            </button>
        </form>

        <ul>
            {
                programs.map((program, index) => {
                    return <li key = { index }>{ program }</li>
                })
            }
        </ul>

        <div>
            <h3>Input Data About Sections:</h3>
        </div>

        <form name = "sections" id = "sections">
            <TextField label = "Section ID: " value = { Section } setValue={addSection}/>
            <TextField label = "Course ID: " value = { Section } setValue={addSection}/>
            <TextField label = "Semester: " value = { Section } setValue={addSection}/>
            <TextField label = "Year: " value = { Section } setValue={addSection}/>
            <TextField label = "Faculty Lead ID: " value = { Section } setValue={addSection}/>
            <TextField label = "Enrollment Count: " value = { Section } setValue={addSection}/>
            <button
                type = "button"
                onClick = {() => {
                    getPrograms(Section)
                }}
            >
                Update Section Information
            </button>
        </form>

        <ul>
            {
                programs.map((program, index) => {
                    return <li key = { index }>{ program }</li>
                })
            }
        </ul>

        <div>
            <h3>Input Data About Learning Objectives:</h3>
        </div>
    

        <form name = "objectives" id = "objectives">
            <TextField label = "Objective ID: " value = { Objective } setValue={addObjective}/>
            <TextField label = "Objective Code: " value = { Objective } setValue={addObjective}/>
            <TextField label = "Description: " value = { Objective } setValue={addObjective}/>
            <TextField label = "Department ID:" value = { Objective } setValue={addObjective}/>
            <button
                type = "button"
                onClick = {() => {
                    getPrograms(Objective)
                }}
            >
                Update Objective Information
            </button>
        </form>

        <ul>
            {
                programs.map((program, index) => {
                    return <li key = { index }>{ program }</li>
                })
            }
        </ul>

        <div>
            <h3>Input Data About Learning Sub-objectives:</h3>
        </div>

        <form name = "sub-objective" id = "sub-objective">
            <TextField label = "Sub-Objective ID: " value = { SubObjective } setValue={addSubObjective}/>
            <TextField label = "Sub-Objective Code: " value = { SubObjective } setValue={addSubObjective}/>
            <TextField label = "Description: " value = { SubObjective } setValue={addSubObjective}/>
            <TextField label = "Parent Objective ID: " value = { SubObjective } setValue={addSubObjective}/>
            <button
                type = "button"
                onClick = {() => {
                    getPrograms(SubObjective)
                }}
            >
                Update Sub-Objective Information
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