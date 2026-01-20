from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError,jwt

from app.core.config import settings

outh2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

def get_current_user(token : str = Depends(outh2_scheme)):
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=['HS256']
        )
        return payload
    except JWTError: 
        raise HTTPException(status_code=401,detail='invalid token')