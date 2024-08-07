from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from datetime import timedelta, datetime
from typing import Union
from database.database import get_db
from models import UserModel
from schemas import UserCreate
from Service import LoginService
from passlib.context import CryptContext
from dotenv import load_dotenv
import os


router = APIRouter(prefix="/login", tags=["login"]) 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#leer variables de entorno
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')



def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db, identifier, password):
    if "@" in identifier:
        user = LoginService.get_user_by_email(db, identifier)
    else:
        user = LoginService.get_user_by_telefono(db, identifier)

    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado", headers={"WWW-Authenticate": "Bearer"})
    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta", headers={"WWW-Authenticate": "Bearer"})
    return user

# Crear token
def create_token(data: dict, time_expire: Union[datetime, None] = None):
    data_copy = data.copy()
    if time_expire is None:
        expire = datetime.utcnow + timedelta(seconds=3600)
    else:
        expire = datetime.utcnow() + time_expire
    data_copy.update({"exp": expire })

    token_jwt= jwt.encode(data_copy, key=SECRET_KEY, algorithm=ALGORITHM)
    print(token_jwt)
    return token_jwt

def get_user_current(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401, detail="No se pudo validar las credenciales", headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        token_decoded = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        email = token_decoded.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = LoginService.get_user_by_email(db, email=email)
    if not user:
        raise credentials_exception
    return user

def get_user_disabled_current(user: UserModel = Depends(get_user_current)):
    print(f"Verificando si el usuario {user.email} está deshabilitado: {user.disable}")
    if user.disable:
        raise HTTPException(status_code=400, detail="Usuario deshabilitado")
    return user

# Autenticacion
@router.post("/login/")
async def user(user: UserModel = Depends(get_user_disabled_current)):
    return user

# Crear ruta token
@router.post("/token/")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    user_dict = {
        "email": user.email,
        "telefono": user.telefono,
        "hashed_password": user.hashed_password,
        "disable": user.disable
    }
    print(user_dict)
    access_token_expires = timedelta(seconds=30)
    print(access_token_expires)
    access_token_jw = create_token({"sub": user.email}, access_token_expires)
    return {
        "access_token": access_token_jw,
        "token_type": "bearer",
        "rol" : user.rol,
        "id": user.id_user,
        "nombre_usuario": user.nombre_usuario,
        "apellido_usuario": user.apellido_usuario,
        "email": user.email,
        
    }

# Crear usuario
@router.post("/users/")
async def create_new_user(user: UserCreate, db: Session = Depends(get_db),):
    db_user = LoginService.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Usuario ya registrado")
    return LoginService.create_user(db, user)

#Ver Usuario
@router.get("/users/me/")
async def get_user(db: Session = Depends(get_db),user: UserModel = Depends(get_user_disabled_current)):
    return LoginService.get_users(db=db)