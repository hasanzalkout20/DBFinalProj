import requests

base_url = 'http://localhost:8000'  # Adjust as needed

# Sample Data for Testing Data Entry
departments = [
    {"DeptName": "Computer Science", "DeptCode": "CSCI"},  # Changed from "deptCode" to "DeptCode"
    {"DeptName": "Mathematics", "DeptCode": "MATH"}        # Changed from "deptCode" to "DeptCode"
]

faculty = [
    {"Name": "John Doe", "Email": "jdoe@csci.edu", "DeptID": 1, "Position": "Associate Professor"},  # Changed keys to start with uppercase
    {"Name": "Jane Smith", "Email": "jsmith@math.edu", "DeptID": 2, "Position": "Professor"}          # Changed keys to start with uppercase
]

programs = [
    {"ProgName": "CS Masters", "DeptID": 1, "FacultyLeadID": 1, "FacultyLeadEmail": "jdoe@csci.edu"},  # Changed keys to start with uppercase
    {"ProgName": "Math PhD", "DeptID": 2, "FacultyLeadID": 2, "FacultyLeadEmail": "jsmith@math.edu"}   # Changed keys to start with uppercase
]

courses = [
    {"DeptID": 1, "CourseID": "CSCI1100", "Title": "Advanced Algorithms", "Description": "Study of advanced algorithmic techniques."},  # Changed keys to start with uppercase
    {"DeptID": 2, "CourseID": "MATH2200", "Title": "Linear Algebra", "Description": "In-depth look at linear algebra and its applications."}  # Changed keys to start with uppercase
]

sections = [
    {"CourseID": "CSCI1100", "Semester": "Fall", "Year": 2022, "FacultyLeadID": 1, "EnrollCount": 30},  # Changed keys to start with uppercase
    {"CourseID": "MATH2200", "Semester": "Spring", "Year": 2023, "FacultyLeadID": 2, "EnrollCount": 25}   # Changed keys to start with uppercase
]

objectives = [
    {"ObjCode": "OBJ101", "Description": "Learn advanced algorithms", "DeptID": 1},  # Changed keys to start with uppercase
    {"ObjCode": "OBJ102", "Description": "Understand linear algebra applications", "DeptID": 2}  # Changed keys to start with uppercase
]

subobjectives = [
    {"SubObjCode": "SUBOBJ101.1", "Description": "Implement graph algorithms", "ParentObjID": 1},  # Changed keys to start with uppercase
    {"SubObjCode": "SUBOBJ102.1", "Description": "Matrix operations and applications", "ParentObjID": 2}  # Changed keys to start with uppercase
]

# Updated to use correct CourseID format
course_objectives = [
    {"CourseID": "CSCI1100", "ObjID": 1},  # Changed keys to start with uppercase
    {"CourseID": "MATH2200", "ObjID": 2}   # Changed keys to start with uppercase
]

# Dummy data for ProgramCourses and CourseProgramObjectives
program_courses = [
    {"ProgID": 1, "CourseID": "CSCI1100"},  # Changed keys to start with uppercase
    {"ProgID": 2, "CourseID": "MATH2200"}   # Changed keys to start with uppercase
]

course_program_objectives = [
    {"CourseID": "CSCI1100", "ProgID": 1, "ObjID": 1},  # Changed keys to start with uppercase
    {"CourseID": "MATH2200", "ProgID": 2, "ObjID": 2}   # Changed keys to start with uppercase
]

# Revised Evaluation Results Section (assuming courseObjID are auto-incremented and start from 1)
evaluation_results = [
    {"CourseObjID": 1, "SecID": 1, "Semester": "Fall", "Year": 2022, "EvalMethod": "Exam", "StudentsPassed": 28},  # Changed keys to start with uppercase
    {"CourseObjID": 2, "SecID": 2, "Semester": "Spring", "Year": 2023, "EvalMethod": "Project", "StudentsPassed": 23}  # Changed keys to start with uppercase
]

# POST Requests for Data Entry
for dept in departments:
    requests.post(f'{base_url}/department', json=dept)

for fac in faculty:
    requests.post(f'{base_url}/faculty', json=fac)

for prog in programs:
    requests.post(f'{base_url}/programs', json=prog)

for course in courses:
    requests.post(f'{base_url}/course', json=course)

for section in sections:
    requests.post(f'{base_url}/section', json=section)

for obj in objectives:
    requests.post(f'{base_url}/objective', json=obj)

for subobj in subobjectives:
    requests.post(f'{base_url}/subobjective', json=subobj)

for co in course_objectives:
    requests.post(f'{base_url}/courseobjective', json=co)

for eval_result in evaluation_results:
    requests.post(f'{base_url}/evaluationresult', json=eval_result)
    
for pc in program_courses:
    requests.post(f'{base_url}/link_course_program', json=pc)

for cpo in course_program_objectives:
    requests.post(f'{base_url}/assign_objective', json=cpo)

# GET Requests for Data Querying
dept_programs = requests.get(f'{base_url}/programs', params={'department_name': 'Mathematics'}).json()
# print programs
print("Department Programs:", dept_programs)
dept_faculty = requests.get(f'{base_url}/faculty', params={'department_name': 'Computer Science'}).json()
# eval_results = requests.get(f'{base_url}/evaluation', params={'course_name': 'Advanced Algorithms', 'semester': 'Fall', 'year': 2022}).json()

# # Displaying the fetched data
print("Department Programs:", dept_programs)
print("Department Faculty:", dept_faculty)
# print("Evaluation Results:", eval_results)

# # Additional GET Requests to Test Querying Functionalities

# # Test: Listing all programs for a given department
response = requests.get(f'{base_url}/programs', params={'department_name': 'Computer Science'})
print("Programs in Computer Science Department:", response.json())

# # Test: Listing all faculty in a given department
response = requests.get(f'{base_url}/faculty', params={'department_name': 'Computer Science'})
print("Faculty in Computer Science Department:", response.json())

# # # Test: Listing evaluation results for each section of a course in a given semester and program
# response = requests.get(f'{base_url}/evaluation', params={'course_name': 'Advanced Algorithms', 'semester': 'Fall', 'year': 2022})
# print("Evaluation Results for Advanced Algorithms in Fall 2022:", response.json())

# Test: Listing evaluation results for each objective/sub-objective for an academic year
response = requests.get(f'{base_url}/evaluation_year', params={'year': 2022})
print("Evaluation Results for Academic Year 2022:", response.json())

# Test: Listing all courses and their objectives for a given program
response = requests.get(f'{base_url}/program_courses_objectives', params={'program_name': 'CS Masters'})
print("Courses and Objectives for CS Masters Program:", response.json())

# Test: Listing all objectives for a given program
response = requests.get(f'{base_url}/program_objectives', params={'program_name': 'Math PhD'})
print("Objectives for Math PhD Program:", response.json())

response = requests.get(f'{base_url}/evaluation_program_semester', params={'program_name': 'CS Masters', 'semester': 'Fall', 'year': 2022})
print("Evaluation Results for CS Masters in Fall 2022:", response.json())


