"""Capa Repositories: acceso a datos de la tabla `vehiculos`."""
from typing import Optional

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.vehiculo import Vehiculo


def crear(db: Session, datos: dict) -> Vehiculo:
    vehiculo = Vehiculo(**datos)
    db.add(vehiculo)
    db.commit()
    db.refresh(vehiculo)
    return vehiculo


def listar(db: Session, tipo: Optional[str] = None) -> list[Vehiculo]:
    consulta = db.query(Vehiculo)
    if tipo:  # FILTRO: por tipo, sin distinguir mayúsculas/minúsculas
        consulta = consulta.filter(func.lower(Vehiculo.tipo) == tipo.strip().lower())
    return consulta.order_by(Vehiculo.id).all()


def obtener_por_id(db: Session, vehiculo_id: int) -> Optional[Vehiculo]:
    return db.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).first()


def obtener_por_placa(db: Session, placa: str) -> Optional[Vehiculo]:
    return db.query(Vehiculo).filter(Vehiculo.placa == placa).first()


def guardar(db: Session, vehiculo: Vehiculo) -> Vehiculo:
    db.commit()
    db.refresh(vehiculo)
    return vehiculo


def eliminar(db: Session, vehiculo: Vehiculo) -> None:
    db.delete(vehiculo)
    db.commit()
