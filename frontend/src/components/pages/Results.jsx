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

    // Check form names and id
    return <>
        
        <div>
            <h3> Add:</h3>
        </div>
       
        <form name = "programs" id = "programs">
            <button
                type = "button"
                onClick = {() => {
                    getPrograms(department)
                }}
            >
                Add Department
            </button>

            <button
                type = "button"
                onClick = {() => {
                    getPrograms(department)
                }}
            >
                Add Faculty
            </button>

            <button
                type = "button"
                onClick = {() => {
                    getPrograms(department)
                }}
            >
                Add Program
            </button>

            <button
                type = "button"
                onClick = {() => {
                    getPrograms(department)
                }}
            >
                Add Course
            </button>

            <button
                type = "button"
                onClick = {() => {
                    getPrograms(department)
                }}
            >
                Add Section
            </button>

            <button
                type = "button"
                onClick = {() => {
                    getPrograms(department)
                }}
            >
                Add Objective
            </button>

            <button
                type = "button"
                onClick = {() => {
                    getPrograms(department)
                }}
            >
                Add Sub-Objective
            </button>

        </form>

        <div>
            <h3>Assign:</h3>
        </div>

        <form name = "programs" id = "programs"> 
            <button
                type = "button"
                onClick = {() => {
                    getPrograms(department)
                }}
            >
                Assign a Learning Objective
            </button>

            <button
                type = "button"
                onClick = {() => {
                    getPrograms(department)
                }}
            >
                Assign a Course
            </button>

        </form>

        <div>
            <h3>Display:</h3>
        </div>

        <form name = "programs" id = "programs"> 
            <button
                type = "button"
                onClick = {() => {
                    getPrograms(department)
                }}
            >
                Show Programs
            </button>
            
            <button
                type = "button"
                onClick = {() => {
                    getPrograms(department)
                }}
            >
                Show Courses
            </button>

            <button
                type = "button"
                onClick = {() => {
                    getPrograms(department)
                }}
            >
                Show Courses
            </button>

            <button
                type = "button"
                onClick = {() => {
                    getPrograms(department)
                }}
            >
                Show Evaluation Results from Program
            </button>

            <button
                type = "button"
                onClick = {() => {
                    getPrograms(department)
                }}
            >
                Show Evaluation Results from Dates
            </button>
            
        </form>



        <div>
            <h3>Input Information to Add Department:</h3>
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
                Add Department
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
            <h3>Input Information to Add Faculty:</h3>
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
                Add Faculty
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
            <h3>Input Information to Add Program:</h3>
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
                Add Program
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
            <h3>Input Information to Add Course:</h3>
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
                Add Course
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
            <h3>Input Information to Add Section:</h3>
        </div>

        Section ID: 
        
        <select
            label="Section ID: "
            value={Section}
            onChange={(e) => addSection(e.target.value)}
        >
            {/* Generating options from 001 to 999 */}
            {[...Array(999).keys()].map((index) => {
                const optionValue = `00${index + 1}`.slice(-3); // Pads the number with leading zeros
                return (
                    <option key={optionValue} value={optionValue}>
                        {optionValue}
                    </option>
                );
            })}
        </select>
        
        <form name = "sections" id = "sections">
            
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
                Add Section
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
            <h3>Input Information to Add Learning Objective:</h3>
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
                Add Learning Objective
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
            <h3>Input Information to Add Learning Sub-objectives:</h3>
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
                Add Sub-Objective
            </button>
        </form>

        <ul>
            {
                programs.map((program, index) => {
                    return <li key = { index }>{ program }</li>
                })
            }
        </ul>


        Querying: 

        Given a Department
        List all its programs
        List all its faculty (including what program each faculty is in charge of, if there is one)

        Given a Program
        List all courses, together with the objectives/sub-objctives assocaition with year
        List all the objectives

        Given a semester and a program:
        List all evaluation results for each section (if data for some sections has not been entered, just indicate that the information is not found)
        
        Given an academic year
        List all evaluation results for each objective/sub-objective
            For each obj/sub-obj, list the course/section that are in involved with evaluating them and list the resutl for each course/section
            For each objective/sub-objective, aggregate the result to show that number (and the percentage) of students
    </>


}