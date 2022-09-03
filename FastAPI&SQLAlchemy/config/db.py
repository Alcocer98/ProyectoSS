from sqlalchemy import create_engine, MetaData 

#Create Engine requiere de una URL como localhost

engine = create_engine('sqlite:///ejemplo.db',connect_args={'check_same_thread': False})

meta = MetaData()

conn = engine.connect()