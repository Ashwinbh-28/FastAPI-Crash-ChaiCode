from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()

class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=3, description="The name of the employee")
    department: Optional[str] = "General"
    salary: float = Field(..., ge=10000)

# In-memory details/ database
employees: List[Employee] = []

# root
@app.get("/")
def read_root():
    return {"Hello": "World"}

# CRUD Operations

# Create employee
@app.post("/employees", response_model=Employee)
def create_employee(employee: Employee):
    # Check for duplicate IDs
    for emp in employees:
        if emp.id == employee.id:
            raise HTTPException(status_code=400, detail="Employee with this ID already exists")
    employees.append(employee)
    return employee

# Get all employees
@app.get("/employees", response_model=List[Employee])
def get_employees():
    return employees

# Get employee by ID
@app.get("/employees/{emp_id}", response_model=Employee)
def get_employee(emp_id: int):
    for emp in employees:
        if emp_id == emp.id:
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

# Update department by employee ID
@app.put("/employees/{emp_id}", response_model=Employee)
def update_dep(emp_id: int, dep: str):
    for emp in employees:
        if emp_id == emp.id:
            emp.department = dep
            return emp
    raise HTTPException(status_code=404, detail="Employee not found")

# Delete employee
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    for idx, emp in enumerate(employees):
        if emp.id == employee_id:
            employees.pop(idx)
            return {"message": f"Employee {employee_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")
