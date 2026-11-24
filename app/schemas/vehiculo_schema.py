"""Capa Schemas: validan los datos de entrada y salida de vehículos."""
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, field_validator


class VehiculoBase(BaseModel):
    placa: str = Field(..., min_length=5, max_length=10, examples=["ABC123"])
    marca: str = Field(..., min_length=1, max_length=50, examples=["Chevrolet"])
    modelo: str = Field(..., min_length=1, max_length=50, examples=["NPR"])
    anio: int = Field(..., ge=1950, le=2100, examples=[2022])
    tipo: str = Field(..., min_length=1, max_length=50, examples=["Camión"])

    @field_validator("placa")
    @classmethod
    def placa_en_mayuscula(cls, v: str) -> str:
        return v.strip().upper()


class VehiculoCrear(VehiculoBase):
    pass


class VehiculoActualizar(BaseModel):
    placa: Optional[str] = Field(None, min_length=5, max_length=10)
    marca: Optional[str] = Field(None, min_length=1, max_length=50)
    modelo: Optional[str] = Field(None, min_length=1, max_length=50)
    anio: Optional[int] = Field(None, ge=1950, le=2100)
    tipo: Optional[str] = Field(None, min_length=1, max_length=50)

    @field_validator("placa")
    @classmethod
    def placa_en_mayuscula(cls, v):
        return v.strip().upper() if v else v


class VehiculoRespuesta(VehiculoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
