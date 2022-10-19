from fastapi import FastAPI 
from routes.user import user 

app = FastAPI(
    title = "API para negocio",
    description = "Esta es la base de la API para el negocio a implementar",
    version = "0.0.1",
    openapi_tags=[{
        'name':"users",
        'description':"users routes"
    }]
)

app.include_router(user) # Incluimos las rutas de user del archivo user.py



if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
