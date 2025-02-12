""" Creaccion de tarjeta de credito"""

class Pago:
    def __init__(self, tarjeta):
        self.tarjeta = tarjeta

    def autoriza_pago(self, nombre):
        if self.tarjeta.get_nombre() == nombre:
            return True
        else:
            return False

class TarjetaCredito:
    def __init__(self, nombre, fecha_vto, numero, codigo):
        self.nombre = nombre
        self.fecha_vto = fecha_vto
        self.numero = numero
        self.codigo = codigo

    def get_numero(self):
        return self.numero
    
    def get_nombre(self):
        return self.nombre
    
    def check_codigo(self, codigo):
        if self.codigo == codigo:
            return True
        else:
            return False
        
tarjeta_Carol = TarjetaCredito("Carol", "09/25", "123467890", "123")
print(tarjeta_Carol.get_nombre())

pago_compra_X = Pago(tarjeta_Carol)
print(pago_compra_X.autoriza_pago("Carol"))
