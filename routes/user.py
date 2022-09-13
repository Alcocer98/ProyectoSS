from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from starlette.responses import RedirectResponse # Redireccionador a una URL deseada
from sqlalchemy.orm import Session
from typing import List
from config.db import SessionLocal, engine # Importamos la conexión
# De la carpeta models y archivo users importamos la variable users (Tabla)
from schemas.user import User as scUser
from crud.crud import sort_users_by_name,get_user_by_id, get_users

user = APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@user.get("/", tags=["Default"])
def main():
    return RedirectResponse(url="/docs") #para generar la documentación y testeo de las rutas

#Obtenemos los datos ordenados por nombre
@user.get('/Users', tags=["users"])
def show_user(db:Session=Depends(get_db)):
    data = get_users(db)
    return data 

#Añadir elementos a la BD
@user.get('/Users/name', tags=["users"]) 
def show_sort(db:Session=Depends(get_db)):
    target_sort = sort_users_by_name(db)
    return target_sort

#Obtenemos un usuario específico
@user.get('/Users/{id}', tags=["users"])
def get_user(id:int,db:Session=Depends(get_db)):
    target = get_user_by_id(db, id = id)
    if target is None:
        raise HTTPException(status_code = 400, detail = "user not found in the db")
    return {"id":target.id, "name":target.name, "email":target.email} # Mostramos las columnas que nos interesan de todos los usuarios 

    