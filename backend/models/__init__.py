class Socio:
    def __init__(self, id: int, nombre: str, cedula: str):
        self.id = id
        self.nombre = nombre
        self.cedula = cedula


class Cuenta:
    def __init__(self, id: int, numero: str, saldo: float, socio_id: int):
        self.id = id
        self.numero = numero
        self.saldo = saldo
        self.socio_id = socio_id


class Asiento:
    def __init__(self, id: int, descripcion: str, monto: float):
        self.id = id
        self.descripcion = descripcion
        self.monto = monto
