from pydantic import BaseModel

# User Schemas
class UserBase(BaseModel):
    email: str
    telefono: str
    nombre_usuario: str
    apellido_usuario: str
    cedula: str
    rol: str
    disable: bool = False

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id_user: int

    class Config:
        from_attributes = True