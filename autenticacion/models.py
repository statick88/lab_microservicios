from sqlalchemy import Column, Integer, String, ForeignKey, Time, DateTime, LargeBinary, Float
from sqlalchemy.types import Boolean,TypeDecorator
from database.database import Base
from sqlalchemy.orm import relationship

#cLase User
class UserModel(Base):
    __tablename__ = 'user'

    id_user = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(70))
    telefono = Column(String(10), nullable=False)
    nombre_usuario = Column(String(50))
    apellido_usuario = Column(String(50))
    cedula = Column(String(10), nullable=False)
    rol = Column(String(15), nullable=False)
    disable = Column(Boolean, default=False)