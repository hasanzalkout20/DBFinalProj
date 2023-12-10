import requests

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
    {"ProgramName": "Computer Science", "DeptCode": "CS", "FacultyLeadName": "John Doe", "FacultyLeadID": 1, "FacultyLeadEmail": "john@university.edu"},
    {"ProgramName": "Electrical Engineering", "DeptCode": "EE", "FacultyLeadName": "Jane Smith", "FacultyLeadID": 2, "FacultyLeadEmail": "jane@university.edu"}
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
    {"ObjCode": "CSOBJ1", "Description": "Understand basic CS concepts", "ProgramName": "Computer Science"},
    {"ObjCode": "EEOBJ1", "Description": "Understand basic EE concepts", "ProgramName": "Electrical Engineering"}
]

subobjectives = [
    {"SubObjCode": "CSOBJ1.1", "Description": "Learn programming fundamentals", "ObjCode": "CSOBJ1"},
    {"SubObjCode": "EEOBJ1.1", "Description": "Learn circuit basics", "ObjCode": "EEOBJ1"}
]

course_objectives = [
    {"CourseID": "CS101", "ObjCode": "CSOBJ1", "SubObjCode": "CSOBJ1.1"},
    {"CourseID": "EE101", "ObjCode": "EEOBJ1", "SubObjCode": "EEOBJ1.1"}
]

evaluation_results = [
    {"ObjEvalID": 1, "CourseObjID": 1, "SectionID": "CS101-001", "EvalMethod": "Exam", "StudentsPassed": 28},
    {"ObjEvalID": 2, "CourseObjID": 2, "SectionID": "EE101-001", "EvalMethod": "Project", "StudentsPassed": 23}
]

# Helper function to send POST requests
def send_post_request(endpoint, data):
    response = requests.post(f"{base_url}/{endpoint}", json=data)
    return response.json()

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
        print(send_post_request("evaluationresult", evaluation_result))
        
if __name__ == "__main__":
    test_data_entry()
        
        

