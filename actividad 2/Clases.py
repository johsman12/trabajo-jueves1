# 7. Sistema de reservas de un gimnasio
class Cliente:
    def __init__(self, nombre, membresia_activa):
        self.nombre = nombre
        self.membresia_activa = membresia_activa
        
    def puede_entrenar(self):
        return self.membresia_activa

# 8. Carrito de compras
class CarritoCompras:
    def __init__(self):
        self.productos = []
        
    def agregar_producto(self, nombre, precio):
        self.productos.append({"nombre": nombre, "precio": precio})
        
    def total(self):
        return sum(p["precio"] for p in self.productos)

# 9. Vehículo de una app de transporte
class Vehiculo:
    def __init__(self, placa, conductor, disponible=True):
        self.placa = placa
        self.conductor = conductor
        self.disponible = disponible
        
    def cambiar_estado(self):
        self.disponible = not self.disponible