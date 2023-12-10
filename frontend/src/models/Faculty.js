// used for the add_department api
export class Faculty {
    constructor(FacultyID, Name, Email, DeptCode, Position) {
        this.FacultyID = FacultyID;
        this.Name = Name; 
        this.Email = Email; 
        // changed: this.DeptID =  DeptID; 
        this.DeptCode = DeptCode;
        this.Position =  Position; 
    }
}