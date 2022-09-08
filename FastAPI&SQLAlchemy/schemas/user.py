#Añadir tipos de datos
from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id : Optional[int]
    name : str
    email : str
    
    class Config:
        orm_mode = True
