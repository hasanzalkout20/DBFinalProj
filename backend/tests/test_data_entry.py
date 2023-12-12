import requests
from json.decoder import JSONDecodeError

base_url = 'http://localhost:8000'  # Adjust as needed

# Test Data
departments = [
    {"DeptCode": "CS", "DeptName": "Computer Science"},
    {"DeptCode": "EE", "DeptName": "Electrical Engineering"}
]

faculties = [
    {"FacultyID": 1, "Name": "John Doe", "Email": "john@university.edu", "DeptCode": "CS", "Position": "Full"},
    {"FacultyID": 2, "Name": "Jane Smith", "Email": "jane@university.edu", "DeptCode": "EE", "Position": "Associate"}
]

programs = [
    {"ProgramName": "CS B.S.", "DeptCode": "CS", "FacultyLeadName": "John Doe", "FacultyLeadID": 1, "FacultyLeadEmail": "john@university.edu"},
    {"ProgramName": "EE B.S.", "DeptCode": "EE", "FacultyLeadName": "Jane Smith", "FacultyLeadID": 2, "FacultyLeadEmail": "jane@university.edu"}
]

courses = [
    {"CourseID": "CS101", "DeptCode": "CS", "Title": "Introduction to Computer Science", "Description": "Basics of CS"},
    {"CourseID": "EE101", "DeptCode": "EE", "Title": "Introduction to Electrical Engineering", "Description": "Basics of EE"}
]

sections = [
    {"SectionID": "CS101-001", "CourseID": "CS101", "Semester": "Fall", "Year": 2023, "FacultyLeadID": 1, "EnrollCount": 30},
    {"SectionID": "EE101-001", "CourseID": "EE101", "Semester": "Spring", "Year": 2023, "FacultyLeadID": 2, "EnrollCount": 25}
]

objectives = [
    {"ObjCode": "CSOBJ1", "Description": "Understand basic CS concepts", "ProgramName": "CS B.S."},
    {"ObjCode": "EEOBJ1", "Description": "Understand basic EE concepts", "ProgramName": "EE B.S."}
]

subobjectives = [
    {"SubObjCode": "CSOBJ1.1", "Description": "Learn programming fundamentals", "ObjCode": "CSOBJ1"},
    {"SubObjCode": "EEOBJ1.1", "Description": "Learn circuit basics", "ObjCode": "EEOBJ1"}
]

course_objectives = [
    {"CourseObjID": 1, "CourseID": "CS101", "ObjCode": "CSOBJ1", "SubObjCode": "CSOBJ1.1"},
    {"CourseObjID": 2, "CourseID": "EE101", "ObjCode": "EEOBJ1", "SubObjCode": "EEOBJ1.1"}
]

evaluation_results = [
    {"ObjEvalID": 1, "CourseObjID": 1, "SectionID": "CS101-001", "EvalMethod": "Exam", "Semester": "Fall", "Year": 2023, "StudentsPassed": 25},
    {"ObjEvalID": 2, "CourseObjID": 1, "SectionID": "CS101-001", "EvalMethod": "Homework", "Semester": "Fall", "Year": 2023, "StudentsPassed": 30},
]

# Helper function to send POST requests
def send_post_request(endpoint, data):
    response = requests.post(f"{base_url}/{endpoint}", json=data)
    try:
        # Check if the response content type is JSON
        if response.headers['Content-Type'] == 'application/json':
            return response.json()
        else:
            return {"error": "Non-JSON response received", "status_code": response.status_code, "response": response.text}
    except JSONDecodeError:
        return {"error": "JSONDecodeError", "status_code": response.status_code, "response": response.text}

# Helper function to send GET requests
def send_get_request(endpoint, params=None):
    response = requests.get(f"{base_url}/{endpoint}", params=params)
    try:
        if response.headers['Content-Type'] == 'application/json':
            return response.json()
        else:
            return {"error": "Non-JSON response received", "status_code": response.status_code, "response": response.text}
    except JSONDecodeError:
        return {"error": "JSONDecodeError", "status_code": response.status_code, "response": response.text}
    
# Test Function
def test_data_entry():
    # Insert departments
    for dept in departments:
        print(send_post_request("department", dept))

    # Insert faculty
    for faculty in faculties:
        print(send_post_request("faculty", faculty))

    # Insert programs
    for program in programs:
        print(send_post_request("program", program))

    # Insert courses
    for course in courses:
        print(send_post_request("course", course))

    # Insert sections
    for section in sections:
        print(send_post_request("section", section))

    # Insert objectives
    for objective in objectives:
        print(send_post_request("objective", objective))

    # Insert subobjectives
    for subobjective in subobjectives:
        print(send_post_request("subobjective", subobjective))

    # Link course to objectives
    for course_objective in course_objectives:
        print(send_post_request("courseobjective", course_objective))

    # Add evaluation results
    for evaluation_result in evaluation_results:
        print(send_post_request("evaluation", evaluation_result))

# Query Test Functions
def test_department_details():
    for dept in departments:
        deptCode = dept['DeptCode']
        print(f"Department Details for {deptCode}:")
        print(send_get_request("department/details", params={"deptCode": deptCode}))

def test_program_courses_and_objectives():
    for program in programs:
        programName = program['ProgramName']
        print(f"Program Courses and Objectives for {programName}:")
        print(send_get_request("program/courses_objectives", params={"programName": programName}))

def test_evaluation_results_by_semester_and_program():
    # Example: Testing for the Fall semester of 2023 for the Computer Science program
    print("Evaluation Results for Fall 2023, Computer Science:")
    print(send_get_request("program/evaluation_results", params={"semester": "Fall", "year": "2023", "programName": "CS B.S."}))

def test_evaluation_results_by_academic_year():
    # Example: Testing for the academic year 2023-2024
    print("Evaluation Results for Academic Year 2023-2024:")
    print(send_get_request("objectives/evaluation_results", params={"startYear": "2023", "endYear": "2024"}))

if __name__ == "__main__":
    test_data_entry()
    test_department_details()
    test_program_courses_and_objectives()
    test_evaluation_results_by_semester_and_program()
    test_evaluation_results_by_academic_year()
        
        

