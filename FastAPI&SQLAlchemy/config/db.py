from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker #Requerido para implementar ORM
from sqlalchemy.ext.declarative import declarative_base

#Create Engine requiere de una URL como localhost

engine = create_engine('sqlite:///ejemplo1.db') #connect_args={'check_same_thread': False}

SessionLocal = sessionmaker(bind = engine)

Base = declarative_base()

