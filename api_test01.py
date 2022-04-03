#todo importando la librera de fastapi
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
    name : str
    sueldo:float
    state : Optional[bool] =None

"""
#TODO metodos
#todo GET .-
#todo POST .-
#todo DELETE
#todo PUT
"""

#todo creando nuestra primera ruta que escuchara nuestro servidor
@app.get("/")
def read_root():
    return {"Hello":"World FastApi Version 01"}


@app.get("/employees/{employee_id}")
def read_employees(employee_id:int,q:Optional[str]=None):
    return {"employee_id":employee_id,"q":q}

@app.post("/employees/{employee_id}")
def update_employees(employee_id:int,employee:Item):
    return {"employee_name":employee.name,"employee_id":employee_id}



