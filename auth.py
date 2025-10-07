from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    if isinstance(password, bytes):
        password = password.decode('utf-8', errors='ignore')
    password = password[:72]
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)

def create_jwt(payload: dict, secret: str, algorithm: str, exp_delta) -> str:
    payload_copy = payload.copy()
    payload_copy["exp"] = datetime.utcnow() + exp_delta
    return jwt.encode(payload_copy, secret, algorithm=algorithm)

def decode_jwt(token: str, secret: str, algorithms):
    return jwt.decode(token, secret, algorithms=algorithms)
