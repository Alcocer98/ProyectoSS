from fastapi import APIRouter
from fastapi.params import Depends
from starlette.responses import RedirectResponse # Redireccionador a una URL deseada
from sqlalchemy.orm import Session
from typing import List
from config.db import SessionLocal,engine # Importamos la conexión
from models.user import User # De la carpeta models y archivo users importamos la variable users (Tabla)
from schemas.user import User as scUser


user = APIRouter()

def get_db():
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()


@user.get("/", tags=["Default"])
def main():
    return RedirectResponse(url="/docs")


# Obtenemos todos los datos de la tabla
@user.get('/Users/',response_model=List[scUser], tags=["Users"])
def show_user(db:Session=Depends(get_db)):
    all_data = db.query(User).all()
    return all_data

#Obtenemos los datos ordenados por nombre
@user.get('/Users/name',response_model=List[scUser], tags=["Users"])
def show_sort(db:Session=Depends(get_db)):
    target_sort = db.query(User).order_by(User.name).all() #Obtenemos todos los datos en orden por nombre
    return target_sort

#Obtenemos un usuario específico
@user.get('/Users/{id}', tags=["Users"])
def show_sort(id:str,db:Session=Depends(get_db)):
    target = db.query(User).filter(User.id == id).first() #Obtenemos el usuario que coincieda con el id
    #return target
    return target.id, target.name, target.email # Mostramos las columnas que nos interesan de todos los usuarios 
