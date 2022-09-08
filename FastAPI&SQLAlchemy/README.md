# Requerimientos

Vamos a usar FastAPI, uvicorn, PyMySQL, cryptography y SQLAlchemy , es importante haber tenido un ambiente virtual creado previamente (conda, py, etc.). Para eviatr encender y apagar uvicorn por cada modificación que se haga se recomienda hacer:

```
uvicorn app:app --reload
```

Posteriormente tendremos un arreglo de carpetas de la forma:

- **routes:** Se guardarán las urls (funciones de ruta).
- **models:** Se guardarán los modelos de datos usados para la base de datos. 
- **chemas:** Definiremos los datos que se van a devolver al cliente y los que se van a recibir de este mismo.
- **config:** Servirá para poder manejar la configuración de la conexión a la base de datos .

Para tener las opciones de FastAPI bemeos de ir a la URL que nos proporciona uvicorn añadiendo al final /docs.

Consideraciones de los submódulos de FASTAPI:
**APIRouter:** Permite definir rutas/subrutas por separado [Página de referencia](https://fastapi.tiangolo.com/tutorial/first-steps/)

# V0.0.2

- Implementación de ORM
- Eliminación de los métodos put, delete y post
- implementación de filtros

