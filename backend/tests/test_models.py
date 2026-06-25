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