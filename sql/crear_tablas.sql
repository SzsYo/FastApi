-- Opcional: la API ya crea las tablas sola al arrancar. Útil para evidencia en el SQL Editor de Neon.
CREATE TABLE IF NOT EXISTS usuarios (
    id         SERIAL PRIMARY KEY,
    nombre     VARCHAR(100) NOT NULL,
    correo     VARCHAR(150) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS vehiculos (
    id     SERIAL PRIMARY KEY,
    placa  VARCHAR(10) NOT NULL UNIQUE,
    marca  VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    anio   INTEGER NOT NULL,
    tipo   VARCHAR(50) NOT NULL
);
