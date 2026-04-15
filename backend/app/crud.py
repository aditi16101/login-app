from sqlalchemy.orm import Session
from . import models, auth

def create_user(db: Session, username: str, password: str):
    hashed = auth.hash_password(password)
    user = models.User(username=username, password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()