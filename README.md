# API de Vehículos y Usuarios (FastAPI + PostgreSQL en Neon)

API REST desarrollada con **Python y FastAPI**, conectada a **PostgreSQL en Neon** y desplegada en **Render**.
Incluye un CRUD de usuarios (contraseñas con hash bcrypt) y el CRUD del Ejercicio 6: gestión de vehículos
(con filtro por tipo). Arquitectura por capas: routes, services, repositories, models, schemas y database.

## Ejecutar en local
```bash
python -m venv venv
venv\Scripts\activate          # Windows  (Linux/Mac: source venv/bin/activate)
pip install -r requirements.txt
copy .env.example .env         # y pega tu DATABASE_URL de Neon
uvicorn main:app --reload
```
Documentación Swagger: http://127.0.0.1:8000/docs

## Endpoints
| Método | Endpoint | Descripción |
|---|---|---|
| POST | /usuarios/ | Registrar usuario |
| GET | /usuarios/ | Listar usuarios |
| GET | /usuarios/{id} | Consultar usuario |
| PUT | /usuarios/{id} | Actualizar usuario |
| DELETE | /usuarios/{id} | Eliminar usuario |
| POST | /vehiculos/ | Registrar vehículo |
| GET | /vehiculos/ | Listar vehículos (`?tipo=Camión` para filtrar) |
| GET | /vehiculos/{id} | Consultar vehículo |
| PUT | /vehiculos/{id} | Actualizar vehículo |
| DELETE | /vehiculos/{id} | Eliminar vehículo |

## Variables de entorno
- `DATABASE_URL`: cadena de conexión de Neon.

## Despliegue en Render
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
