from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.models.user import User
from app.schemas.auth import UserRegister,UserLogin,TokenResponse
from app.core.security import hash_password,verify_password
from app.auth.jwt import create_access_token,create_refresh_token


router = APIRouter(prefix='/auth',tags=["auth"])

@router.post("/register",status_code=201)
def register(data : UserRegister,db : Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == data.email).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail= "email already exists!"
        )
    user = User(
        email = data.email,
        hashed_password = hash_password(data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return {'message': 'User Created'}

@router.post('/login',response_model=TokenResponse)
def login(data: UserLogin, db : Session =Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail= 'invalid credentials'
        )
    return {
        'access_token' : create_access_token(str(user.id)),
        'refresh_token': create_refresh_token(str(user.id))
    }
