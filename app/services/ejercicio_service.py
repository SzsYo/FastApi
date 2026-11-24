"""Capa Services (Ejercicio 6): lógica de negocio de vehículos."""
from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import ejercicio_repository as repo
from app.schemas.vehiculo_schema import VehiculoActualizar, VehiculoCrear


def crear_vehiculo(db: Session, datos: VehiculoCrear):
    if repo.obtener_por_placa(db, datos.placa):  # regla: placa única
        raise HTTPException(status.HTTP_409_CONFLICT, "Ya existe un vehículo con esa placa")
    return repo.crear(db, datos.model_dump())


def listar_vehiculos(db: Session, tipo: Optional[str] = None):
    return repo.listar(db, tipo)


def obtener_vehiculo(db: Session, vehiculo_id: int):
    vehiculo = repo.obtener_por_id(db, vehiculo_id)
    if not vehiculo:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Vehículo no encontrado")
    return vehiculo


def actualizar_vehiculo(db: Session, vehiculo_id: int, datos: VehiculoActualizar):
    vehiculo = obtener_vehiculo(db, vehiculo_id)
    cambios = datos.model_dump(exclude_unset=True)
    if not cambios:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "No se envió ningún campo para actualizar")

    if "placa" in cambios:
        existente = repo.obtener_por_placa(db, cambios["placa"])
        if existente and existente.id != vehiculo_id:
            raise HTTPException(status.HTTP_409_CONFLICT, "Ya existe un vehículo con esa placa")
    for campo, valor in cambios.items():
        setattr(vehiculo, campo, valor)
    return repo.guardar(db, vehiculo)


def eliminar_vehiculo(db: Session, vehiculo_id: int) -> None:
    repo.eliminar(db, obtener_vehiculo(db, vehiculo_id))
