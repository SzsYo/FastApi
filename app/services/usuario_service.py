"""Capa Services: lógica de negocio de usuarios (reglas, hash, errores HTTP)."""
import bcrypt
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import usuario_repository as repo
from app.schemas.usuario_schema import UsuarioActualizar, UsuarioCrear


def _hashear(contrasena: str) -> str:
    return bcrypt.hashpw(contrasena.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def crear_usuario(db: Session, datos: UsuarioCrear):
    correo = datos.correo.lower()
    if repo.obtener_por_correo(db, correo):  # regla: correo único
        raise HTTPException(status.HTTP_409_CONFLICT, "Ya existe un usuario con ese correo")
    return repo.crear(db, datos.nombre.strip(), correo, _hashear(datos.contrasena))


def listar_usuarios(db: Session):
    return repo.listar(db)


def obtener_usuario(db: Session, usuario_id: int):
    usuario = repo.obtener_por_id(db, usuario_id)
    if not usuario:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Usuario no encontrado")
    return usuario


def actualizar_usuario(db: Session, usuario_id: int, datos: UsuarioActualizar):
    usuario = obtener_usuario(db, usuario_id)
    cambios = datos.model_dump(exclude_unset=True)
    if not cambios:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "No se envió ningún campo para actualizar")

    if "correo" in cambios:
        nuevo = cambios["correo"].lower()
        existente = repo.obtener_por_correo(db, nuevo)
        if existente and existente.id != usuario_id:
            raise HTTPException(status.HTTP_409_CONFLICT, "Ya existe un usuario con ese correo")
        usuario.correo = nuevo
    if "nombre" in cambios:
        usuario.nombre = cambios["nombre"].strip()
    if "contrasena" in cambios:
        usuario.contrasena = _hashear(cambios["contrasena"])
    return repo.guardar(db, usuario)


def eliminar_usuario(db: Session, usuario_id: int) -> None:
    repo.eliminar(db, obtener_usuario(db, usuario_id))
