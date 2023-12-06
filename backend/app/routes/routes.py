from app import app
from app.models.model import Model
from flask import request, jsonify

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

# POST routes for adding data to the database

@app.route("/department", methods=["POST"])
def addDepartment():
    model = Model()
    deptName = request.json.get("deptName")
    deptCode = request.json.get("deptCode")
    model.insert_department(deptName, deptCode)
    return jsonify({"message": "Department added successfully"}), 201

@app.route("/faculty", methods=["POST"])
def addFaculty():
    model = Model()
    name = request.json.get("name")
    email = request.json.get("email")
    deptID = request.json.get("deptID")
    position = request.json.get("position")
    model.insert_faculty(name, email, deptID, position)
    return jsonify({"message": "Faculty added successfully"}), 201

@app.route("/program", methods=["POST"])
def addProgram():
    model = Model()
    progName = request.json.get("progName")
    deptID = request.json.get("deptID")
    facultyLeadID = request.json.get("facultyLeadID")
    facultyLeadEmail = request.json.get("facultyLeadEmail")
    model.insert_program(progName, deptID, facultyLeadID, facultyLeadEmail)
    return jsonify({"message": "Program added successfully"}), 201

@app.route("/course", methods=["POST"])
def addCourse():
    model = Model()
    deptID = request.json.get("deptID")
    title = request.json.get("title")
    description = request.json.get("description")
    model.insert_course(deptID, title, description)
    return jsonify({"message": "Course added successfully"}), 201

@app.route("/section", methods=["POST"])
def addSection():
    model = Model()
    courseID = request.json.get("courseID")
    semester = request.json.get("semester")
    year = request.json.get("year")
    facultyLeadID = request.json.get("facultyLeadID")
    enrollCount = request.json.get("enrollCount")
    model.insert_section(courseID, semester, year, facultyLeadID, enrollCount)
    return jsonify({"message": "Section added successfully"}), 201

@app.route("/objective", methods=["POST"])
def addObjective():
    model = Model()
    objCode = request.json.get("objCode")
    description = request.json.get("description")
    deptID = request.json.get("deptID")
    model.insert_objective(objCode, description, deptID)
    return jsonify({"message": "Objective added successfully"}), 201

@app.route("/subobjective", methods=["POST"])
def addSubobjective():
    model = Model()
    subObjCode = request.json.get("subObjCode")
    description = request.json.get("description")
    parentObjID = request.json.get("parentObjID")
    model.insert_subobjective(subObjCode, description, parentObjID)
    return jsonify({"message": "Subobjective added successfully"}), 201

@app.route("/courseobjective", methods=["POST"])
def linkCourseObjective():
    model = Model()
    courseID = request.json.get("courseID")
    objID = request.json.get("objID")
    model.link_course_to_objective(courseID, objID)
    return jsonify({"message": "Course linked to objective successfully"}), 201

@app.route("/evaluationresult", methods=["POST"])
def addEvaluationResult():
    model = Model()
    courseObjID = request.json.get("courseObjID")
    secID = request.json.get("secID")
    semester = request.json.get("semester")
    year = request.json.get("year")
    evalMethod = request.json.get("evalMethod")
    studentsPassed = request.json.get("studentsPassed")
    model.insert_evaluation_result(courseObjID, secID, semester, year, evalMethod, studentsPassed)
    return jsonify({"message": "Evaluation result added successfully"}), 201
