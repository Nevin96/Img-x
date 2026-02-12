from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer,HTTPBearer,HTTPAuthorizationCredentials
from jose import JWTError,jwt

from app.core.config import settings

security = HTTPBearer()
# outh2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

def get_current_user(credentials : HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=['HS256']
        )
        return payload['sub']
    except JWTError: 
        raise HTTPException(status_code=401,detail='invalid token')