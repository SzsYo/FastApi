"""Capa Models: tabla `vehiculos` en PostgreSQL."""
from sqlalchemy import Column, Integer, String

from app.database.conexion import Base


class Vehiculo(Base):
    __tablename__ = "vehiculos"

    id = Column(Integer, primary_key=True, index=True)
    placa = Column(String(10), unique=True, nullable=False, index=True)
    marca = Column(String(50), nullable=False)
    modelo = Column(String(50), nullable=False)
    anio = Column(Integer, nullable=False)
    tipo = Column(String(50), nullable=False, index=True)
