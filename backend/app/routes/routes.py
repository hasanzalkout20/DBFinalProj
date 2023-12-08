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

@app.route("/programs", methods=["GET"])
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

@app.route("/evaluation", methods=["GET"])
def getEvaluation():
    model = Model()
    course_name = request.args.get("course_name")
    semester = request.args.get("semester")
    year = request.args.get("year")
    results = model.getEvaluationResultsByCourseName(course_name, semester, year)
    return jsonify(results)

@app.route("/evaluation_program_semester", methods=["GET"])
def getEvaluationByProgramAndSemester():
    model = Model()
    program_name = request.args.get("program_name")
    semester = request.args.get("semester")
    year = request.args.get("year")
    results = model.getEvaluationResultsByProgramAndSemester(program_name, semester, year)
    if not results:
        return jsonify({"message": "No data found for the specified parameters"}), 404
    return jsonify(results)


@app.route("/evaluation_year", methods=["GET"])
def getEvaluationByYear():
    model = Model()
    academic_year = request.args.get("year")
    results = model.getEvaluationResultsByAcademicYear(academic_year)
    return jsonify(results)

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

# Department POST route with duplicate prevention and error handling
@app.route("/department", methods=["POST"])
def addDepartment():
    model = Model()
    deptName = request.json.get("DeptName")
    deptCode = request.json.get("DeptCode")
    result = model.insert_department(deptName, deptCode)
    status_code = get_status_code(result)
    return jsonify(result), status_code

# Faculty POST route with duplicate prevention and error handling
@app.route("/faculty", methods=["POST"])
def addFaculty():
    model = Model()
    name = request.json.get("Name")
    email = request.json.get("Email")
    deptID = request.json.get("DeptID")
    position = request.json.get("Position")
    result = model.insert_faculty(name, email, deptID, position)
    status_code = get_status_code(result)
    return jsonify(result), status_code

# Program POST route with duplicate prevention and error handling
@app.route("/program", methods=["POST"])
def addProgram():
    model = Model()
    progName = request.json.get("ProgName")
    deptID = request.json.get("DeptID")
    facultyLeadID = request.json.get("FacultyLeadID")
    facultyLeadEmail = request.json.get("FacultyLeadEmail")
    result = model.insert_program(progName, deptID, facultyLeadID, facultyLeadEmail)
    status_code = get_status_code(result)
    return jsonify(result), status_code

# Course POST route with duplicate prevention and error handling
@app.route("/course", methods=["POST"])
def addCourse():
    model = Model()
    courseID = request.json.get("CourseID")  # Updated to use CourseID directly
    title = request.json.get("Title")
    description = request.json.get("Description")
    deptID = request.json.get("DeptID")
    result = model.insert_course(courseID, title, description, deptID)
    status_code = get_status_code(result)
    return jsonify(result), status_code

# Updated POST route for sections
@app.route("/section", methods=["POST"])
def addSection():
    model = Model()
    courseID = request.json.get("CourseID")
    semester = request.json.get("Semester")
    year = request.json.get("Year")
    facultyLeadID = request.json.get("FacultyLeadID")
    enrollCount = request.json.get("EnrollCount")
    result = model.insert_section(courseID, semester, year, facultyLeadID, enrollCount)
    status_code = get_status_code(result)
    return jsonify(result), status_code

# Objective POST route with duplicate prevention and error handling
@app.route("/objective", methods=["POST"])
def addObjective():
    model = Model()
    objCode = request.json.get("ObjCode")
    description = request.json.get("Description")
    deptID = request.json.get("DeptID")
    result = model.insert_objective(objCode, description, deptID)
    status_code = get_status_code(result)
    return jsonify(result), status_code

# Subobjective POST route with duplicate prevention and error handling
@app.route("/subobjective", methods=["POST"])
def addSubobjective():
    model = Model()
    subObjCode = request.json.get("SubObjCode")
    description = request.json.get("Description")
    parentObjID = request.json.get("ParentObjID")
    result = model.insert_subobjective(subObjCode, description, parentObjID)
    status_code = get_status_code(result)
    return jsonify(result), status_code

# CourseObjective POST route with duplicate prevention and error handling
@app.route("/courseobjective", methods=["POST"])
def linkCourseObjective():
    model = Model()
    courseID = request.json.get("CourseID")
    objID = request.json.get("ObjID")
    result = model.link_course_to_objective(courseID, objID)
    status_code = get_status_code(result)
    return jsonify(result), status_code

# EvaluationResult POST route with duplicate prevention and error handling
@app.route("/evaluationresult", methods=["POST"])
def addEvaluationResult():
    model = Model()
    courseObjID = request.json.get("CourseObjID")
    secID = request.json.get("SecID")
    semester = request.json.get("Semester")
    year = request.json.get("Year")
    evalMethod = request.json.get("EvalMethod")
    studentsPassed = request.json.get("StudentsPassed")
    result = model.insert_evaluation_result(courseObjID, secID, semester, year, evalMethod, studentsPassed)
    status_code = get_status_code(result)
    return jsonify(result), status_code

# LinkCourseToProgram POST route with duplicate prevention and error handling
@app.route("/link_course_program", methods=["POST"])
def linkCourseToProgram():
    model = Model()
    ProgID = request.json.get("ProgID")
    courseID = request.json.get("CourseID")
    result = model.link_course_to_program(ProgID, courseID)
    status_code = get_status_code(result)
    return jsonify(result), status_code

# AssignObjectiveToCourseProgram POST route with duplicate prevention and error handling
@app.route("/assign_objective", methods=["POST"])
def assignObjectiveToCourseProgram():
    model = Model()
    courseID = request.json.get("CourseID")
    ProgID = request.json.get("ProgID")
    objID = request.json.get("ObjID")
    result = model.assign_objective_to_course_program(courseID, ProgID, objID)
    status_code = get_status_code(result)
    return jsonify(result), status_code

if __name__ == "__main__":
    app.run(debug=True)




