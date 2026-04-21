from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    confirm_password: str

class UserLogin(BaseModel):
    username: str
    password: str

class ResetPassword(BaseModel):
    username: str
    new_password: str