from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# --- Modelos de datos (Pydantic) ---
class DepositoRequest(BaseModel):
    socio_id: int
    monto: float
    descripcion: str

class DepositoResponse(BaseModel):
    transaccion_id: int
    socio_id: int
    tipo: str
    monto: float
    saldo_nuevo: float
    fecha: datetime
    descripcion: str

class CreditoRequest(BaseModel):
    socio_id: int
    monto_solicitado: float
    plazo_meses: int
    tasa_interes: float
    motivo: str
    garantia: Optional[str] = None

class CreditoResponse(BaseModel):
    solicitud_id: int
    socio_id: int
    estado: str
    monto_aprobado: Optional[float]
    plazo_meses: int
    tasa_interes: float
    fecha_solicitud: datetime
    mensaje: str

# --- FastAPI App ---
app = FastAPI(
    title="Sistema Caja de Ahorros - Grupo 05",
    description="Backend para la gestión de socios, cuentas de ahorro, créditos y transacciones.",
    version="1.0.0"
)

# --- Endpoints existentes ---
@app.get("/")
def inicio():
    return {"mensaje": "Backend del Sistema Caja de Ahorros funcionando"}

@app.get("/socios")
def listar_socios():
    return [
        {"id": 1, "nombre": "Juan Perez", "cedula": "0912345678"},
        {"id": 2, "nombre": "Maria Lopez", "cedula": "0923456789"}
    ]

@app.get("/cuentas")
def listar_cuentas():
    return [
        {"id": 1, "numero": "CA-001", "saldo": 150.00, "socio_id": 1},
        {"id": 2, "numero": "CA-002", "saldo": 300.00, "socio_id": 2}
    ]

# --- Nuevos endpoints de la Sección 3 ---
@app.post("/api/transacciones/deposito", status_code=status.HTTP_200_OK)
async def deposito(request: DepositoRequest):
    """Endpoint para registrar un depósito en la cuenta de un socio."""
    try:
        if request.monto <= 0:
            raise HTTPException(status_code=400, detail="El monto debe ser mayor a 0")
        
        # Simulación: buscar socio y actualizar saldo
        # Aquí iría la lógica real con base de datos
        saldo_actual = 1250.75  # Esto vendría de la BD
        nuevo_saldo = saldo_actual + request.monto
        
        response = DepositoResponse(
            transaccion_id=5,
            socio_id=request.socio_id,
            tipo="deposito",
            monto=request.monto,
            saldo_nuevo=nuevo_saldo,
            fecha=datetime.now(),
            descripcion=request.descripcion
        )
        return {"status": "success", "data": response}
        
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

@app.get("/api/socios/{id}/saldo")
async def obtener_saldo(id: int):
    """Endpoint para consultar el saldo actual de un socio."""
    try:
        if id <= 0:
            raise HTTPException(status_code=404, detail="Socio no encontrado")
            
        # Simulación de datos del socio
        socios = {
            1: {"nombre": "Juan Perez", "cedula": "0912345678", "saldo": 1250.75},
            2: {"nombre": "Maria Lopez", "cedula": "0923456789", "saldo": 300.00}
        }
        
        socio = socios.get(id)
        if not socio:
            raise HTTPException(status_code=404, detail="Socio no encontrado")
            
        return {
            "status": "success",
            "data": {
                "socio_id": id,
                "nombre": socio["nombre"],
                "cedula": socio["cedula"],
                "saldo_actual": socio["saldo"],
                "saldo_disponible": socio["saldo"],
                "fecha_consulta": datetime.now()
            }
        }
        
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

@app.post("/api/creditos/solicitud", status_code=status.HTTP_201_CREATED)
async def solicitud_credito(request: CreditoRequest):
    """Endpoint para registrar una solicitud de crédito."""
    try:
        if request.monto_solicitado <= 0:
            raise HTTPException(status_code=400, detail="El monto solicitado debe ser mayor a 0")
            
        if request.plazo_meses <= 0 or request.plazo_meses > 60:
            raise HTTPException(status_code=400, detail="El plazo debe estar entre 1 y 60 meses")
        
        # Simulación: validar socio existe
        socios_validos = [1, 2]
        if request.socio_id not in socios_validos:
            raise HTTPException(status_code=404, detail="Socio no encontrado")
        
        # Datos de la solicitud
        response = CreditoResponse(
            solicitud_id=10,
            socio_id=request.socio_id,
            estado="pendiente",
            monto_aprobado=None,
            plazo_meses=request.plazo_meses,
            tasa_interes=request.tasa_interes,
            fecha_solicitud=datetime.now(),
            mensaje="Solicitud de crédito registrada exitosamente. Espera aprobación del comité."
        )
        
        return {"status": "success", "data": response}
        
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
