"""Capa Models: tabla `usuarios` en PostgreSQL."""
from sqlalchemy import Column, Integer, String

from app.database.conexion import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(150), unique=True, nullable=False, index=True)
    contrasena = Column(String(255), nullable=False)  # aquí se guarda el HASH, nunca el texto plano
