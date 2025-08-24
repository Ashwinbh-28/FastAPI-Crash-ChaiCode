from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic model = defines structure of Employee
class Employee(BaseModel):
    id: int
    name: str
    role: str
    salary: float

# local database
db: List[Employee] = []


# ---- Deserialization Example ----
@app.post("/add_employee")
def add_employee(emp: Employee):
    """
    Input: JSON from frontend
    Deserialization: JSON → Python object (Employee model)
    """
    db.append(emp)
    print("Python object after deserialization:", emp)
    return {"message": "Employee added successfully", "employee": emp}


# ---- Serialization Example ----
@app.get("/get_employee")
def get_employee():
    """
    Python object → JSON response
    Serialization: Employee model → JSON
    """
    return db

# Put method testing
@app.put("/update_salary/{emp_id}")
def update_salary(emp_id: int, new_salary: float):
    """
    Deserialization: emp_id from path + salary from query params
    Serialization: Updated employee as JSON response
    """
    for emp in db:
        if emp.id == emp_id:
            emp.salary = new_salary   # update in Python object
            print("Updated Salary:", emp.salary)
            return {"message": "Salary updated", "employee": emp}
    return {"error": "Employee not found"}
