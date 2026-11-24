from fastapi import FastAPI

from app.database.conexion import Base, engine
from app.models import usuario, vehiculo  # noqa: F401  (registra las tablas en Base)
from app.routes import ejercicio, usuarios

# Crea las tablas en Neon si todavía no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Vehículos y Usuarios",
    description="API REST con FastAPI y PostgreSQL (Neon). Ejercicio 6: gestión de vehículos.",
    version="1.0.0",
)

app.include_router(usuarios.router)
app.include_router(ejercicio.router)


@app.get("/", tags=["Inicio"])
def inicio():
    return {"mensaje": "API funcionando", "documentacion": "/docs"}
