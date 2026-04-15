from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

MAX_LEN = 72

def hash_password(password: str):
    password = password[:MAX_LEN]   # truncate safely
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    plain = plain[:MAX_LEN]
    return pwd_context.verify(plain, hashed)