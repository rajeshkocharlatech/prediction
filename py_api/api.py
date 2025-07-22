from fastapi import FastAPI, HTTPException
import pandas as pd

# Initialize FastAPI app
app = FastAPI()

# Load  CSV data
try:
    _csv_data = pd.read_csv("C:/Users/Admin/Desktop/AI/My_Projects/Dataset/college_student_placement_dataset.csv")
    student_data = _csv_data.to_dict(orient='records')
except FileNotFoundError:
    student_data = []
    print("CSV file not found. Ensure the file path is correct.")

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Student API from CSV using FastAPI"}

# Endpoint to get all students
@app.get("/students")
def get_students():
    if not student_data:
        raise HTTPException(status_code=404, detail="No student data available")
    return student_data

# Endpoint to get a student by ID
@app.get("/students/{student_id}")
def get_student_by_id(student_id: int):
    if student_id < 0 or student_id >= len(student_data):
        raise HTTPException(status_code=404, detail="Student not found")
    return student_data[student_id]