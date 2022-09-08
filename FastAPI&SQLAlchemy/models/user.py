from sqlalchemy import Column, Integer, String
from config.db import engine, Base

#Columnas a crear de SQLite

class User(Base):
    __tablename__ = "Usuarios" #Nombre de la tabla

    id = Column(Integer, primary_key=True) 
    name = Column(String(255))
    email = Column(String(255))


Base.metadata.create_all(bind=engine) # Genera la tabla en SQLite
