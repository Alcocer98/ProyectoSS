from fastapi import APIRouter, Response, status
from config.db import conn # Importamos la conexión
from models.user import users # De la carpeta models y archivo users importamos la variable users (Tabla)
from schemas.user import User
from starlette.status import HTTP_204_NO_CONTENT 

from cryptography.fernet import Fernet #Cifrador de contraseñas

key = Fernet.generate_key() #Únicos cada uno de los cifrados que hagamos
f = Fernet(key)

user = APIRouter()

#Mostramos nuestra tabla
@user.get('/users',response_model= list[User], tags=["users"])
def get_user():
    return conn.execute(users.select()).fetchall() #Nuestra Querry a toda la tabla (equivalente a un SELECT * FROM)


#Añadir elementos a la BD
@user.post('/users', response_model=User, tags=["users"]) 
def create_user(user: User):
    new_user = {"name":user.name,"email":user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user)) # Guardamos en la BD
    
    # Vamos a ejecutar una consulta select, de la cual seleccionará donde la columna ID del usuario
    # sea igual al último ID, y sólo el primer elemento (devuelve una lista).
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first() 


#Petición de un usuario muy específico
@user.get('/users/{id}', response_model = User, tags=["users"])
def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first() 


#Petición de borrado
@user.delete('/users/{id}',status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


#Actualizar 
@user.put('/users/{id}',response_model=User, tags=["users"])
def update_user(id:str,user:User):
    conn.execute(users.update().values(name = user.name, email = user.email, password = f.encrypt(user.password.encode("utf-8"))).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()