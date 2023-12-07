import requests

base_url = 'http://127.0.0.1:8000'  # Adjust as needed

# Sample Data for Testing Data Entry
departments = [
    {"deptName": "Computer Science", "deptCode": "CSCI"},
    {"deptName": "Mathematics", "deptCode": "MATH"}
]

faculty = [
    {"name": "John Doe", "email": "jdoe@csci.edu", "deptID": 1, "position": "Associate Professor"},
    {"name": "Jane Smith", "email": "jsmith@math.edu", "deptID": 2, "position": "Professor"}
]

programs = [
    {"progName": "CS Masters", "deptID": 1, "facultyLeadID": 1, "facultyLeadEmail": "jdoe@csci.edu"},
    {"progName": "Math PhD", "deptID": 2, "facultyLeadID": 2, "facultyLeadEmail": "jsmith@math.edu"}
]

courses = [
    {"deptID": 1, "title": "Advanced Algorithms", "description": "Study of advanced algorithmic techniques."},
    {"deptID": 2, "title": "Linear Algebra", "description": "In-depth look at linear algebra and its applications."}
]

sections = [
    {"courseID": 1, "semester": "Fall", "year": 2022, "facultyLeadID": 1, "enrollCount": 30},
    {"courseID": 2, "semester": "Spring", "year": 2023, "facultyLeadID": 2, "enrollCount": 25}
]

objectives = [
    {"objCode": "OBJ101", "description": "Learn advanced algorithms", "deptID": 1},
    {"objCode": "OBJ102", "description": "Understand linear algebra applications", "deptID": 2}
]

subobjectives = [
    {"subObjCode": "SUBOBJ101.1", "description": "Implement graph algorithms", "parentObjID": 1},
    {"subObjCode": "SUBOBJ102.1", "description": "Matrix operations and applications", "parentObjID": 2}
]

course_objectives = [
    {"courseID": 1, "objID": 1},
    {"courseID": 2, "objID": 2}
]

evaluation_results = [
    {"courseObjID": 1, "secID": 1, "semester": "Fall", "year": 2022, "evalMethod": "Exam", "studentsPassed": 28},
    {"courseObjID": 2, "secID": 2, "semester": "Spring", "year": 2023, "evalMethod": "Project", "studentsPassed": 23}
]

# POST Requests for Data Entry
for dept in departments:
    requests.post(f'{base_url}/department', json=dept)

for fac in faculty:
    requests.post(f'{base_url}/faculty', json=fac)

for prog in programs:
    requests.post(f'{base_url}/program', json=prog)

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

# GET Requests for Data Querying
dept_programs = requests.get(f'{base_url}/programs', params={'department_name': 'Computer Science'}).json()
dept_faculty = requests.get(f'{base_url}/faculty', params={'department_name': 'Computer Science'}).json()
eval_results = requests.get(f'{base_url}/evaluation', params={'course_name': 'Advanced Algorithms', 'semester': 'Fall', 'year': 2022}).json()

# Displaying the fetched data
print("Department Programs:", dept_programs)
print("Department Faculty:", dept_faculty)
print("Evaluation Results:", eval_results)

# Additional GET Requests for Extended Functionality
academic_year_results = requests.get(f'{base_url}/evaluation_year', params={'year': '2022'}).json()
print("Academic Year Evaluation Results:", academic_year_results)

# Additional GET Requests to Test Querying Functionalities

# Test: Listing all programs for a given department
response = requests.get(f'{base_url}/programs', params={'department_name': 'Computer Science'})
print("Programs in Computer Science Department:", response.json())

# Test: Listing all faculty in a given department
response = requests.get(f'{base_url}/faculty', params={'department_name': 'Computer Science'})
print("Faculty in Computer Science Department:", response.json())

# Test: Listing evaluation results for each section of a course in a given semester and program
response = requests.get(f'{base_url}/evaluation', params={'course_name': 'Advanced Algorithms', 'semester': 'Fall', 'year': 2022})
print("Evaluation Results for Advanced Algorithms in Fall 2022:", response.json())

# Test: Listing evaluation results for each objective/sub-objective for an academic year
response = requests.get(f'{base_url}/evaluation_year', params={'year': 2022})
print("Evaluation Results for Academic Year 2022:", response.json())


# Test: Listing all courses and their objectives for a given program
# Note: Assuming a route and method for this functionality exists, replace 'program_courses_objectives' with the correct endpoint
response = requests.get(f'{base_url}/program_courses_objectives', params={'program_name': 'CS Masters'})
print("Courses and Objectives for CS Masters Program:", response.json())

# Test: Listing all objectives for a given program
# Note: Assuming a route and method for this functionality exists, replace 'program_objectives' with the correct endpoint
response = requests.get(f'{base_url}/program_objectives', params={'program_name': 'CS Masters'})
print("Objectives for CS Masters Program:", response.json())
