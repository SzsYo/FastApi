"""Capa Schemas: validan los datos de entrada y salida de usuarios."""
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UsuarioCrear(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100, examples=["Brandon García"])
    correo: EmailStr = Field(..., examples=["brandon@correo.com"])
    contrasena: str = Field(..., min_length=8, max_length=64, examples=["Clave12345"])


class UsuarioActualizar(BaseModel):
    nombre: Optional[str] = Field(None, min_length=1, max_length=100)
    correo: Optional[EmailStr] = None
    contrasena: Optional[str] = Field(None, min_length=8, max_length=64)


class UsuarioRespuesta(BaseModel):
    """Nunca devuelve la contraseña."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str
    correo: EmailStr
