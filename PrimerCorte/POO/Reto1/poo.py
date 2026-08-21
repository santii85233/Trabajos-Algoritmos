class Usuario:
    def __init__(self, nombre, documento, sanciones):
        self.nombre= nombre
        self.documento = documento
        self.sanciones = False

    def puede_solicitar(self):
        return not self.sanciones

class Recurso:
    def __init__(self,codigo,categoria,disponible):
        self.codigo = codigo
        self.categoria = categoria
        self.disponible = False

class Prestamo:
    def __init__(self, fecha):
        self.fecha = fecha



