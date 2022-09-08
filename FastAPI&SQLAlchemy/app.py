from fastapi import FastAPI 
from routes.user import user # Importamos del archivo user a user


app = FastAPI(
    title = "API para negocio",
    description = "Esta es la base de la API para el negocio a implementar, en formato de ORM.",
    version = "0.0.2", 
    openapi_tags=[{
        'name':"Users",
        'description':"Métodos implementados a los usuarios"
    }]
)

app.include_router(user) # Incluimos las rutas de user del archivo user.py