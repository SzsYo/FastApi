"""Capa Routes (Ejercicio 6): endpoints de /vehiculos."""
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.database.conexion import get_db
from app.schemas.vehiculo_schema import VehiculoActualizar, VehiculoCrear, VehiculoRespuesta
from app.services import ejercicio_service as service

router = APIRouter(prefix="/vehiculos", tags=["Vehículos"])


@router.post("/", response_model=VehiculoRespuesta, status_code=status.HTTP_201_CREATED)
def registrar_vehiculo(datos: VehiculoCrear, db: Session = Depends(get_db)):
    return service.crear_vehiculo(db, datos)


@router.get("/", response_model=list[VehiculoRespuesta])
def consultar_vehiculos(
    tipo: Optional[str] = Query(None, description="Filtra por tipo de vehículo (ej: Camión, Bus)"),
    db: Session = Depends(get_db),
):
    return service.listar_vehiculos(db, tipo)


@router.get("/{id}", response_model=VehiculoRespuesta)
def consultar_vehiculo(id: int, db: Session = Depends(get_db)):
    return service.obtener_vehiculo(db, id)


@router.put("/{id}", response_model=VehiculoRespuesta)
def actualizar_vehiculo(id: int, datos: VehiculoActualizar, db: Session = Depends(get_db)):
    return service.actualizar_vehiculo(db, id, datos)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_vehiculo(id: int, db: Session = Depends(get_db)):
    service.eliminar_vehiculo(db, id)
