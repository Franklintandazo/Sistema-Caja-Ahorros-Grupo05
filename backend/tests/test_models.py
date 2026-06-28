import sys
import os

# Esto asegura que Python pueda encontrar la carpeta 'models' que está un nivel arriba
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos las clases reales de tus modelos
# Asegúrate de que en la carpeta 'models/' exista un archivo con estos nombres o un __init__.py
from models import Socio, Cuenta, Asiento

def test_creacion_socio():
    socio = Socio(id=1, nombre="Juan Perez", cedula="0912345678")
    assert socio.id == 1
    assert socio.nombre == "Juan Perez"
    assert socio.cedula == "0912345678"

def test_creacion_cuenta():
    cuenta = Cuenta(id=1, numero="CA-001", saldo=150.00, socio_id=1)
    assert cuenta.id == 1
    assert cuenta.numero == "CA-001"
    assert cuenta.saldo == 150.00
    assert cuenta.socio_id == 1

def test_creacion_asiento():
    asiento = Asiento(id=1, descripcion="Depósito inicial", monto=150.00)
    assert asiento.id == 1
    assert asiento.descripcion == "Depósito inicial"
    assert asiento.monto == 150.00

def test_cobertura_obligatoria():
    print("Ejecutando test real de modelos para cobertura...")
    # Creamos instancias adicionales para asegurar que coverage detecte estas líneas
    socio = Socio(id=2, nombre="Test", cedula="123")
    cuenta = Cuenta(id=2, numero="002", saldo=0.0, socio_id=2)
    asiento = Asiento(id=2, descripcion="Test", monto=10.0)
    
    assert socio.nombre == "Test"
    assert cuenta.saldo == 0.0
    assert asiento.monto == 10.0