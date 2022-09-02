from fastapi import FastAPI 
from routes.user import user # Importamos del archivo user a user


app = FastAPI(
    title = "API para negocio",
    description = "Esta es la base de la API para el negocio a implementar",
    version = "0.0.1", #Primera versión
    openapi_tags=[{
        'name':"users",
        'description':"users routes"
    }]
)

app.include_router(user) # Incluimos las rutas de user del archivo user.py