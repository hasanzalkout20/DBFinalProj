import requests

base_url = 'http://localhost:8000'  # Adjust as needed

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

# GET Requests to Fetch Data
dept_programs = requests.get(f'{base_url}/programs', params={'department': 'CSCI'}).json()
dept_faculty = requests.get(f'{base_url}/faculty', params={'department': 'CSCI'}).json()
eval_results = requests.get(f'{base_url}/evaluation', params={'semester': 'Fall', 'year': 2022, 'secID': 1}).json()

# Displaying the fetched data
print("Department Programs:", dept_programs)
print("Department Faculty:", dept_faculty)
print("Evaluation Results:", eval_results)

# Add similar requests for objectives, subobjectives, course objectives, and evaluation results
