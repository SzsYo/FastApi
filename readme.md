FastApi
Aprendiz: Brandon Garcia Morales
Ejercicio 6: API para gestion de vehiculos


1. DESCRIPCION
API REST hecha con Python y FastAPI, conectada a una base de datos
PostgreSQL en Neon y desplegada en Render. Permite administrar usuarios
y vehiculos (crear, consultar, actualizar y eliminar).


2. MODULOS
- Usuarios: CRUD obligatorio. No permite correos repetidos y guarda la
  contrasena como hash (nunca en texto plano).
- Vehiculos (Ejercicio 6): CRUD con placa unica y filtro por tipo.


3. ARQUITECTURA POR CAPAS
Cliente -> Routes -> Services -> Repositories -> Neon (PostgreSQL)

- Routes:       recibe las solicitudes y define los endpoints.
- Services:     logica del negocio (duplicados, hash, errores).
- Repositories: consultas a la base de datos.
- Models:       representan las tablas.
- Schemas:      validan los datos de entrada y salida.
- Database:     conexion con Neon.


4. TABLAS
usuarios:  id, nombre, correo (unico), contrasena (hash)
vehiculos: id, placa (unica), marca, modelo, anio, tipo

Las tablas no estan relacionadas entre si.


5. ENDPOINTS
Usuarios:
  POST   /usuarios/          Registrar usuario
  GET    /usuarios/          Consultar usuarios
  GET    /usuarios/{id}      Consultar usuario por ID
  PUT    /usuarios/{id}      Actualizar usuario
  DELETE /usuarios/{id}      Eliminar usuario

Vehiculos:
  POST   /vehiculos/         Registrar vehiculo
  GET    /vehiculos/         Consultar vehiculos
  GET    /vehiculos/?tipo=Bus   Filtrar por tipo
  GET    /vehiculos/{id}     Consultar vehiculo por ID
  PUT    /vehiculos/{id}     Actualizar vehiculo
  DELETE /vehiculos/{id}     Eliminar vehiculo

Codigos HTTP: 200 ok, 201 creado, 204 eliminado, 404 no encontrado,
409 duplicado, 422 datos invalidos.


6. CONEXION CON NEON
La cadena de conexion esta en la variable de entorno DATABASE_URL
(archivo .env en local y Environment Variables en Render).


7. COMO EJECUTAR EN LOCAL
  python -m venv venv
  venv\Scripts\activate
  pip install -r requirements.txt
  copy .env.example .env      (y pegar DATABASE_URL de Neon)
  uvicorn main:app --reload

Documentacion Swagger: http://127.0.0.1:8000/docs


8. DESPLIEGUE EN RENDER
Build Command: pip install -r requirements.txt
Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
Variables:     DATABASE_URL y PYTHON_VERSION=3.12.8