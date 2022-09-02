from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

#Columnas a crear de SQLite
users = Table("users", meta, Column("id", Integer, primary_key=True), 
    Column("name", String(255)), 
    Column("email",String(255)), 
    Column("password", String(255)))

meta.create_all(engine) # Genera la tabla en SQLite
