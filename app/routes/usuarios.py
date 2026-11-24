"""Capa Routes: endpoints de /usuarios. Solo recibe la petición y delega al service."""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.conexion import get_db
from app.schemas.usuario_schema import UsuarioActualizar, UsuarioCrear, UsuarioRespuesta
from app.services import usuario_service as service

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/", response_model=UsuarioRespuesta, status_code=status.HTTP_201_CREATED)
def registrar_usuario(datos: UsuarioCrear, db: Session = Depends(get_db)):
    return service.crear_usuario(db, datos)


@router.get("/", response_model=list[UsuarioRespuesta])
def consultar_usuarios(db: Session = Depends(get_db)):
    return service.listar_usuarios(db)


@router.get("/{id}", response_model=UsuarioRespuesta)
def consultar_usuario(id: int, db: Session = Depends(get_db)):
    return service.obtener_usuario(db, id)


@router.put("/{id}", response_model=UsuarioRespuesta)
def actualizar_usuario(id: int, datos: UsuarioActualizar, db: Session = Depends(get_db)):
    return service.actualizar_usuario(db, id, datos)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(id: int, db: Session = Depends(get_db)):
    service.eliminar_usuario(db, id)
