import requests

base_url = 'http://127.0.0.1:8000'  # Adjust as needed

# Sample Data
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

# POST Requests to Add Data
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


# GET Requests to Fetch Data
dept_programs = requests.get(f'{base_url}/programs', params={'department_name': 'Computer Science'}).json()
dept_faculty = requests.get(f'{base_url}/faculty', params={'department_name': 'Computer Science'}).json()
eval_results = requests.get(f'{base_url}/evaluation', params={'course_name': 'Advanced Algorithms', 'semester': 'Fall', 'year': 2022}).json()

# Displaying the fetched data
print("Department Programs:", dept_programs)
print("Department Faculty:", dept_faculty)
print("Evaluation Results:", eval_results)
