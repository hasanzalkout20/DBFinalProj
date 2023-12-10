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

@app.route("/program", methods=["GET"])
def getDepartmentPrograms():
    model = Model()
    department_name = request.args.get("department_name")
    programs = model.getProgramDepartments(department_name)
    return jsonify(programs)

@app.route("/faculty", methods=["GET"])
def getDepartmentFaculty():
    model = Model()
    department_name = request.args.get("department_name")
    faculty = model.getFacultyByDepartmentName(department_name)
    return jsonify(faculty)

# @app.route("/evaluation", methods=["GET"])
# def getEvaluation():
#     model = Model()
#     course_name = request.args.get("course_name")
#     semester = request.args.get("semester")
#     year = request.args.get("year")
#     results = model.getEvaluationResultsByCourseName(course_name, semester, year)
#     return jsonify(results)

# @app.route("/evaluation_program_semester", methods=["GET"])
# def getEvaluationByProgramAndSemester():
#     model = Model()
#     program_name = request.args.get("program_name")
#     semester = request.args.get("semester")
#     year = request.args.get("year")
#     results = model.getEvaluationResultsByProgramAndSemester(program_name, semester, year)
#     if not results:
#         return jsonify({"message": "No data found for the specified parameters"}), 404
#     return jsonify(results)

@app.route("/evaluation_program_semester", methods=["GET"])
def getEvaluationByProgramAndSemester():
    model = Model()
    program_name = request.args.get("program_name")
    semester = request.args.get("semester")
    year = request.args.get("year")
    results = model.getEvaluationResultsByProgramAndSemester(program_name, semester, year)
    if not results:
        return jsonify({"message": "No data found for the specified parameters"}), 404
    return jsonify({"results": results})

# @app.route("/evaluation_year", methods=["GET"])
# def getEvaluationByYear():
#     model = Model()
#     academic_year = request.args.get("year")
#     results = model.getEvaluationResultsByAcademicYear(academic_year)
#     return jsonify(results)

@app.route("/evaluation_year", methods=["GET"])
def getEvaluationByYear():
    model = Model()
    academic_year = request.args.get("year")
    results = model.getEvaluationResultsByAcademicYear(academic_year)
    if not results:
        return jsonify({"message": "No data found for the specified parameters"}), 404
    return jsonify({"results": results})

@app.route("/program_courses_objectives", methods=["GET"])
def getProgramCoursesObjectives():
    model = Model()
    program_name = request.args.get("program_name")
    results = model.getCoursesAndObjectivesForProgram(program_name)
    return jsonify(results)

@app.route("/program_objectives", methods=["GET"])
def getProgramObjectives():
    model = Model()
    program_name = request.args.get("program_name")
    results = model.getProgramObjectives(program_name)
    return jsonify(results)

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




