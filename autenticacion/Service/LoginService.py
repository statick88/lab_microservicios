from sqlalchemy.orm import Session
from models import UserModel
from schemas import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


################Usuario Login################
#obtener datos user
def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

#obtener datos user telefono
def get_user_by_telefono(db: Session, telefono: int):
    return db.query(UserModel).filter(UserModel.telefono == telefono).first()

#obtener usuarios
def get_users(db: Session):
    return db.query(UserModel).all()

#ingresar datos user
def generate_bcrypt_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.hashed_password)
    db_user = UserModel(
        email=user.email,
        hashed_password=hashed_password,
        telefono=user.telefono,
        nombre_usuario=user.nombre_usuario,
        apellido_usuario=user.apellido_usuario,
        cedula=user.cedula,
        rol=user.rol,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user