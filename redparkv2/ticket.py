from cliente import cliente

class ticket:
    
    nombreConductor: str
    patenteVehiculo: str
    duracion: str
    precio: str
    
    def __init__(self, nombreConductor, patenteVehiculo, duracion, precio):
        
        self.nombreConductor = nombreConductor
        self.patenteVehiculo = patenteVehiculo
        self.duracion = duracion
        self.precio = precio