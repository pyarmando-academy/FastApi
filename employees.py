from fastapi import FastAPI, HTTPException

from pydantic import BaseModel
from typing import Optional, Text
from datetime import datetime
from uuid import uuid4 as uuid

app = FastAPI()

employees = []


class Employees(BaseModel):
    id: Optional[str]
    first_name: str
    last_name: str
    description: Text
    created_at: datetime = datetime.now()
    state: Optional[bool] = True


@app.get('/employees')
def get_employees():
    return employees


@app.post('/employees')
def save_employees(employee: Employees):
    employee.id = str(uuid())
    employees.append(employee.dict())
    return employees[-1]


@app.get('/employees/{employee_id}')
def get_employee(employee_id: str):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
    raise HTTPException(status_code=404, detail="Employee not found")


@app.delete('/employees/{employee_id}')
def delete_employee(employee_id: str):
    for index, employee in enumerate(employees):
        if employee["id"] == employee_id:
            employees.pop(index)
            return {"message": "employee deleted"}
    return HTTPException(status_code=404, detail="Employee not found")


@app.put('/employees/{employee_id}')
def update_employee(employee_id: str, updatedemployee: Employees):
    for index, employee in enumerate(employees):
        if employee["id"] == employee_id:
            employees[index]["first_name"] = updatedemployee.dict()["first_name"]
            employees[index]["last_name"] = updatedemployee.dict()["last_name"]
            employees[index]["description"] = updatedemployee.dict()["description"]
            return {"message": "Employee has been updated succesfully"}
    return HTTPException(status_code=404, detail="Item not found")


# @app.put('/employees/{employee_id}')
# def update_employee(employee_id: str, updatedemployee: Employees):
#     for index, employee in enumerate(employees):
#         if employee["id"] == employee_id:
#             employees[index]["first_name"] = updatedemployee.dict()["first_name"]
#             employees[index]["last_name"] = updatedemployee.dict()["last_name"]
#             employees[index]["description"] = updatedemployee.dict()["description"]
#             return {"message": "employee has been updated succesfully"}
#     raise HTTPException(status_code=404, detail="Item not found")