# Sección 3: Diseño de API - Sistema de Caja de Ahorros

## Visión General
El sistema expone una API RESTful para la gestión de caja de ahorros. Todas las respuestas se entregan en formato JSON y los códigos de estado HTTP siguen los estándares REST.

**Base URL:** `http://localhost:8000/api/`

## Endpoints Clave

### 1. POST /api/transacciones/deposito
**Propósito:** Registrar un depósito en la cuenta de ahorros de un socio.

**Método HTTP:** `POST`

#### Request (JSON esperado):
```json
{
  "socio_id": 1,
  "monto": 150.75,
  "descripcion": "Depósito por transferencia bancaria"
}