from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import schemas, crud, auth

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    print("Register API HIT")

    if user.password != user.confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    existing = crud.get_user(db, user.username)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    return crud.create_user(db, user.username, user.password)

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user.username)
    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}


@router.post("/reset-password")
def reset_password(data: schemas.ResetPassword, db: Session = Depends(get_db)):
    user = crud.update_password(db, data.username, data.new_password)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Password updated successfully"}