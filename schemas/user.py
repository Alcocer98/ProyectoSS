from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id : Optional[int]
    name : str
    email: str
    password: str
    
    class Config:
        orm_mode = True 