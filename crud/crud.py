from models.user import User
from sqlalchemy.orm import Session

#lista de usuarios 
def get_users(db: Session):
    return db.query(User).all()

#ordenar la bd de usarios por nombre
def sort_users_by_name(db: Session):
    return db.query(User).order_by(User.name).all()

#obtener un usuario por id
def get_user_by_id(db: Session, id:int):  
    return db.query(User).filter(User.id == id).first()


