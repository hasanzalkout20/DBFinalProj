from app import app
from app.models.model import Model
from flask import request, jsonify

# Utility function to check if the result contains an error message
def is_error(result):
    return 'error' in result or 'message' in result and 'already exists' in result['message']

# Utility function to determine the HTTP status code based on the result
def get_status_code(result):
    if result.get('message', '').find('already exists') != -1:
        return 409  # Conflict
    if 'error' in result:
        return 500  # Internal Server Error
    return 201  # Created

# GET routes for retrieving data from the database
@app.route("/department/details", methods=["GET"])
def department_details():
    model = Model()
    deptCode = request.args.get("deptCode")
    result = model.get_department_details(deptCode)
    return jsonify(result)

@app.route("/program/courses_objectives", methods=["GET"])
def program_courses_and_objectives():
    model = Model()
    programName = request.args.get("programName")
    result = model.get_program_courses_and_objectives(programName)
    return jsonify(result)

@app.route("/program/evaluation_results", methods=["GET"])
def evaluation_results_by_semester_and_program():
    model = Model()
    semester = request.args.get("semester")
    year = request.args.get("year")
    programName = request.args.get("programName")
    result = model.get_evaluation_results_by_semester_and_program(semester, year, programName)
    return jsonify(result)

@app.route("/objectives/evaluation_results", methods=["GET"])
def evaluation_results_by_academic_year():
    model = Model()
    startYear = request.args.get("startYear")
    endYear = request.args.get("endYear")
    result = model.get_evaluation_results_by_academic_year(startYear, endYear)
    return jsonify(result)

# POST routes for adding data to the database

@app.route("/department", methods=["POST"])
def add_department():
    model = Model()
    deptCode = request.json.get("DeptCode")
    deptName = request.json.get("DeptName")
    result = model.insert_department(deptCode, deptName)
    status_code = get_status_code(result)
    return jsonify(result), status_code

@app.route("/faculty", methods=["POST"])
def add_faculty():
    model = Model()
    facultyID = request.json.get("FacultyID")
    name = request.json.get("Name")
    email = request.json.get("Email")
    deptCode = request.json.get("DeptCode")
    position = request.json.get("Position")
    result = model.insert_faculty(facultyID, name, email, deptCode, position)
    status_code = get_status_code(result)
    return jsonify(result), status_code

@app.route("/program", methods=["POST"])
def add_program():
    model = Model()
    programName = request.json.get("ProgramName")
    deptCode = request.json.get("DeptCode")
    facultyLeadName = request.json.get("FacultyLeadName")
    facultyLeadID = request.json.get("FacultyLeadID")
    facultyLeadEmail = request.json.get("FacultyLeadEmail")
    result = model.insert_program(programName, deptCode, facultyLeadName, facultyLeadID, facultyLeadEmail)
    status_code = get_status_code(result)
    return jsonify(result), status_code

@app.route("/course", methods=["POST"])
def add_course():
    model = Model()
    courseID = request.json.get("CourseID")
    deptCode = request.json.get("DeptCode")
    title = request.json.get("Title")
    description = request.json.get("Description")
    result = model.insert_course(courseID, deptCode, title, description)
    status_code = get_status_code(result)
    return jsonify(result), status_code

@app.route("/section", methods=["POST"])
def add_section():
    model = Model()
    sectionID = request.json.get("SectionID")
    courseID = request.json.get("CourseID")
    semester = request.json.get("Semester")
    year = request.json.get("Year")
    facultyLeadID = request.json.get("FacultyLeadID")
    enrollCount = request.json.get("EnrollCount")
    result = model.insert_section(sectionID, courseID, semester, year, facultyLeadID, enrollCount)
    status_code = get_status_code(result)
    return jsonify(result), status_code

@app.route("/objective", methods=["POST"])
def add_objective():
    model = Model()
    objCode = request.json.get("ObjCode")
    description = request.json.get("Description")
    programName = request.json.get("ProgramName")
    result = model.insert_objective(objCode, description, programName)
    status_code = get_status_code(result)
    return jsonify(result), status_code

@app.route("/subobjective", methods=["POST"])
def add_subobjective():
    model = Model()
    subObjCode = request.json.get("SubObjCode")
    description = request.json.get("Description")
    objCode = request.json.get("ObjCode")
    result = model.insert_subobjective(subObjCode, description, objCode)
    status_code = get_status_code(result)
    return jsonify(result), status_code

@app.route("/courseobjective", methods=["POST"])
def link_course_to_objective():
    model = Model()
    courseID = request.json.get("CourseID")
    objCode = request.json.get("ObjCode")
    subObjCode = request.json.get("SubObjCode")
    result = model.link_course_to_objective(courseID, objCode, subObjCode)
    status_code = get_status_code(result)
    return jsonify(result), status_code

@app.route("/evaluation", methods=["POST"])
def add_evaluation_result():
    model = Model()
    courseObjID = request.json.get("CourseObjID")
    sectionID = request.json.get("SectionID")
    evalMethod = request.json.get("EvalMethod")
    semester = request.json.get("Semester")
    year = request.json.get("Year")
    studentsPassed = request.json.get("StudentsPassed")
    result = model.insert_evaluation_result(courseObjID, sectionID, evalMethod, semester, year, studentsPassed)
    status_code = get_status_code(result)
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(debug=True)
