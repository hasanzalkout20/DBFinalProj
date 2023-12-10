import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()
host = os.environ.get("HOST")
port = os.environ.get("PORT")
database = os.environ.get("DATABASE")
username = os.environ.get("DB_USERNAME")
password = os.environ.get("DB_PASSWORD")

class Model:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    # QUERY METHODS
    def get_department_details(self, deptCode):
        try:
            # Query to get all programs in the department
            self.cursor.execute("SELECT * FROM Program WHERE DeptCode = %s", (deptCode,))
            programs = self.cursor.fetchall()

            # Query to get all faculty in the department
            self.cursor.execute("SELECT * FROM Faculty WHERE DeptCode = %s", (deptCode,))
            faculty = self.cursor.fetchall()

            return {"programs": programs, "faculty": faculty}
        except Error as e:
            return {"error": str(e)}
        
    def get_program_courses_and_objectives(self, programName):
        try:
            # Query to get all courses for the program
            self.cursor.execute("SELECT Course.* FROM Course JOIN Program ON Course.DeptCode = Program.DeptCode WHERE ProgramName = %s", (programName,))
            courses = self.cursor.fetchall()

            # Query to get all objectives for the program
            self.cursor.execute("SELECT * FROM Objectives WHERE ProgramName = %s", (programName,))
            objectives = self.cursor.fetchall()

            # Adjusting the way to get sub-objectives
            subobjectives = {}
            for obj in objectives:
                objCode = obj[0]  # Assuming ObjCode is the first column in the Objectives table
                self.cursor.execute("SELECT * FROM SubObjectives WHERE ObjCode = %s", (objCode,))
                subobjectives[objCode] = self.cursor.fetchall()

            return {"courses": courses, "objectives": objectives, "subobjectives": subobjectives}
        except Error as e:
            return {"error": str(e)}

    def get_evaluation_results_by_semester_and_program(self, semester, year, programName):
        try:
            # Query to get all evaluation results
            self.cursor.execute("""
                SELECT ObjectiveEval.*, Section.CourseID FROM ObjectiveEval
                JOIN Section ON ObjectiveEval.SectionID = Section.SectionID
                JOIN Course ON Section.CourseID = Course.CourseID
                JOIN Program ON Course.DeptCode = Program.DeptCode
                WHERE Section.Semester = %s AND Section.Year = %s AND Program.ProgramName = %s
                """, (semester, year, programName))
            results = self.cursor.fetchall()

            # Handle case where no data found
            if not results:
                return {"message": "No data found"}

            return {"evaluation_results": results}
        except Error as e:
            return {"error": str(e)}

    def get_evaluation_results_by_academic_year(self, startYear, endYear):
        try:
            startYear = int(startYear)
            endYear = int(endYear)
            
            self.cursor.execute("""
                SELECT ObjectiveEval.*, Objectives.ObjCode, Objectives.Description AS ObjDesc, 
                    SubObjectives.SubObjCode, SubObjectives.Description AS SubObjDesc, 
                    Section.EnrollCount
                FROM ObjectiveEval
                JOIN CourseObjectives ON ObjectiveEval.CourseObjID = CourseObjectives.CourseObjID
                JOIN Objectives ON CourseObjectives.ObjCode = Objectives.ObjCode
                LEFT JOIN SubObjectives ON CourseObjectives.SubObjCode = SubObjectives.SubObjCode
                JOIN Section ON ObjectiveEval.SectionID = Section.SectionID
                WHERE ObjectiveEval.Year >= %s AND ObjectiveEval.Year <= %s
                """, (startYear, endYear))
            results = self.cursor.fetchall()

            if not results:
                return {"message": "No data found"}
            
            # Aggregate results
            aggregated_results = {}
            for result in results:
                # Adjust the indices based on the tuple length
                objCode = result[7]  # Index for 'Objectives.ObjCode'
                subObjCode = result[9] if result[9] else 'N/A'  # Index for 'SubObjectives.SubObjCode'
                enrollCount = int(result[11])  # Index for 'Section.EnrollCount'
                studentsPassed = int(result[6])  # Index for 'ObjectiveEval.StudentsPassed'

                key = f"{objCode}_{subObjCode}"
                if key not in aggregated_results:
                    aggregated_results[key] = {'total_students': 0, 'students_passed': 0}
                aggregated_results[key]['total_students'] += enrollCount
                aggregated_results[key]['students_passed'] += studentsPassed

            for key, value in aggregated_results.items():
                value['pass_percentage'] = (value['students_passed'] / value['total_students']) * 100 if value['total_students'] > 0 else 0

            return {"evaluation_results": results, "aggregated_results": aggregated_results}
        except Error as e:
            return {"error": str(e)}

    # DATA ENTRY METHODS

    # Method to insert a new department
    def insert_department(self, deptCode, deptName):
        try:
            self.cursor.execute("SELECT DeptCode FROM Department WHERE DeptCode = %s", (deptCode,))
            if self.cursor.fetchone():
                return {"message": "Department code already exists"}
            sql = "INSERT INTO Department (DeptCode, DeptName) VALUES (%s, %s)"
            self.cursor.execute(sql, (deptCode, deptName))
            self.connection.commit()
            return {"message": "Department added successfully"}
        except Error as e:
            return {"error": str(e)}

    # Method to insert a new faculty member
    def insert_faculty(self, facultyID, name, email, deptCode, position):
        try:
            self.cursor.execute("SELECT FacultyID FROM Faculty WHERE FacultyID = %s OR Email = %s", (facultyID, email))
            if self.cursor.fetchone():
                return {"message": "Faculty member already exists"}
            sql = "INSERT INTO Faculty (FacultyID, Name, Email, DeptCode, Position) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (facultyID, name, email, deptCode, position))
            self.connection.commit()
            return {"message": "Faculty member added successfully"}
        except Error as e:
            return {"error": str(e)}

    # Method to insert a new program
    def insert_program(self, programName, deptCode, facultyLeadName, facultyLeadID, facultyLeadEmail):
        try:
            self.cursor.execute("SELECT ProgramName FROM Program WHERE ProgramName = %s", (programName,))
            if self.cursor.fetchone():
                return {"message": "Program already exists"}
            sql = "INSERT INTO Program (ProgramName, DeptCode, FacultyLeadName, FacultyLeadID, FacultyLeadEmail) VALUES (%s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (programName, deptCode, facultyLeadName, facultyLeadID, facultyLeadEmail))
            self.connection.commit()
            return {"message": "Program added successfully"}
        except Error as e:
            return {"error": str(e)}


    # Method to insert a new course
    def insert_course(self, courseID, deptCode, title, description):
        try:
            self.cursor.execute("SELECT CourseID FROM Course WHERE CourseID = %s", (courseID,))
            if self.cursor.fetchone():
                return {"message": "Course with this ID already exists"}
            sql = "INSERT INTO Course (CourseID, DeptCode, Title, Description) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(sql, (courseID, deptCode, title, description))
            self.connection.commit()
            return {"message": "Course added successfully"}
        except Error as e:
            return {"error": str(e)}

    # Method to insert a new section
    def insert_section(self, sectionID, courseID, semester, year, facultyLeadID, enrollCount):
        try:
            self.cursor.execute("SELECT SectionID FROM Section WHERE SectionID = %s", (sectionID,))
            if self.cursor.fetchone():
                return {"message": "Section ID already exists"}
            sql = "INSERT INTO Section (SectionID, CourseID, Semester, Year, FacultyLeadID, EnrollCount) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (sectionID, courseID, semester, year, facultyLeadID, enrollCount))
            self.connection.commit()
            return {"message": "Section added successfully"}
        except Error as e:
            return {"error": str(e)}

    # Method to insert a new objective
    def insert_objective(self, objCode, description, programName):
        try:
            self.cursor.execute("SELECT ObjCode FROM Objectives WHERE ObjCode = %s", (objCode,))
            if self.cursor.fetchone():
                return {"message": "Objective code already exists"}
            sql = "INSERT INTO Objectives (ObjCode, Description, ProgramName) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (objCode, description, programName))
            self.connection.commit()
            return {"message": "Objective added successfully"}
        except Error as e:
            return {"error": str(e)}

    # Method to insert a new subobjective
    def insert_subobjective(self, subObjCode, description, objCode):
        try:
            self.cursor.execute("SELECT SubObjCode FROM SubObjectives WHERE SubObjCode = %s", (subObjCode,))
            if self.cursor.fetchone():
                return {"message": "Subobjective code already exists"}
            sql = "INSERT INTO SubObjectives (SubObjCode, Description, ObjCode) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (subObjCode, description, objCode))
            self.connection.commit()
            return {"message": "Subobjective added successfully"}
        except Error as e:
            return {"error": str(e)}

    # Method to link a course to an objective
    def link_course_to_objective(self, courseID, objCode, subObjCode=None):
        try:
            self.cursor.execute("SELECT CourseObjID FROM CourseObjectives WHERE CourseID = %s AND ObjCode = %s AND (SubObjCode IS NULL OR SubObjCode = %s)", (courseID, objCode, subObjCode))
            if self.cursor.fetchone():
                return {"message": "Course-objective pair already exists"}
            sql = "INSERT INTO CourseObjectives (CourseID, ObjCode, SubObjCode) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (courseID, objCode, subObjCode))
            self.connection.commit()
            return {"message": "Course-objective pair added successfully"}
        except Error as e:
            return {"error": str(e)}

    # Method to enter evaluation results for a course objective
    def insert_evaluation_result(self, courseObjID, sectionID, evalMethod, semester, year, studentsPassed):
        try:
            self.cursor.execute("SELECT ObjEvalID FROM ObjectiveEval WHERE CourseObjID = %s AND SectionID = %s AND EvalMethod = %s AND Semester = %s AND Year = %s", (courseObjID, sectionID, evalMethod, semester, year))
            if self.cursor.fetchone():
                return {"message": "Evaluation result already exists"}
            sql = "INSERT INTO ObjectiveEval (CourseObjID, SectionID, EvalMethod, Semester, Year, StudentsPassed) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (courseObjID, sectionID, evalMethod, semester, year, studentsPassed))
            self.connection.commit()
            return {"message": "Evaluation result added successfully"}
        except Error as e:
            return {"error": str(e)}





    