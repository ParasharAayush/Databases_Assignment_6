from fastapi import FastAPI, HTTPException
from crud import create_student, get_student, update_student, delete_student

app = FastAPI()

@app.post("/students/")
def create_student_endpoint(student_id: str, name: str, age: int, department: str):
    result = create_student(student_id, name, age, department)
    if result:
        return {"status": "Student created successfully", "student": result}
    raise HTTPException(status_code=400, detail="Student creation failed")

@app.get("/students/{student_id}")
def get_student_endpoint(student_id: str):
    result = get_student(student_id)
    if result:
        return {"status": "Student retrieved successfully", "student": result}
    raise HTTPException(status_code=404, detail="Student not found")

@app.put("/students/{student_id}")
def update_student_endpoint(student_id: str, name: str, age: int, department: str):
    result = update_student(student_id, name, age, department)
    if result:
        return {"status": "Student updated successfully", "student": result}
    raise HTTPException(status_code=400, detail="Student update failed")

@app.delete("/students/{student_id}")
def delete_student_endpoint(student_id: str):
    if delete_student(student_id):
        return {"status": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")

