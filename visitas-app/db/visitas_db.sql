-- Database: visitas_db

-- DROP DATABASE IF EXISTS visitas_db;

CREATE DATABASE visitas_db;

CREATE TABLE visitas (
    id SERIAL PRIMARY KEY,
    ip_cliente VARCHAR(255),
    timestamp TIMESTAMP DEFAULT NOW()
);

CREATE TABLE entorno (
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(50) -- Valores: "development" o "release"
);