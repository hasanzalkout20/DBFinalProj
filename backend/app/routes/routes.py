from app import app
from app.models.model import Model
from flask import request, jsonify

@app.route("/programs", methods = ["GET"])
def getDepartmentPrograms():
    model = Model()
    department = request.args.get("department")
    programs = model.getProgramDepartments(department)
    return jsonify(programs)

@app.route("/faculty", methods = ["GET"])
def getDepartmentFaculty():
    model = Model()
    department = request.args.get("department")
    programs = model.getFacultyDepartments(department)
    return jsonify(programs)

@app.route("/evaluation", methods = ["GET"])
def getEvaluation():
    model = Model()
    semester = request.args.get("semester")
    year = request.args.get("year")
    secID = request.args.get("secID")
    results = model.getEvaluationResults(semester, year, secID)
    return jsonify(results)