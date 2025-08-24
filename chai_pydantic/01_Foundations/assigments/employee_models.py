from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI()

class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=3, description="The name of the employee")
    department: Optional[str] = "General"
    salary: float = Field(..., ge=10000)  # salary >= 10000

# In-memory storage
employees: List[Employee] = []

@app.get("/")
def read_root():
    return {"Hello": "World"}


# POST: Register employee
@app.post("/register")
def register_employee(employee: Employee):
    employees.append(employee)
    return {"message": f"Employee named {employee.name} has been registered"}

# GET: Get all employees
@app.get("/employees")
def get_employees():
    return employees

employees = Employee(
    id=1,
    name="John Doe",
    department="IT",
    salary=50000
)
print(employees)
