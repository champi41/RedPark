import json
import os
class ticket:
    
    nombreConductor: str
    patenteVehiculo: str
    duracion: str
    precio: str
    rut: str
    
    def __init__(self, nombreConductor, patenteVehiculo, duracion, precio, rut):
        
        self.nombreConductor = nombreConductor
        self.rut = rut
        self.patenteVehiculo = patenteVehiculo
        self.duracion = duracion
        self.precio = precio
        #aca tendria que ir el lugar en la amtriz que falta hacer aun
        
    def Crear_Boleta(self):
        ticket_aux = {
            "Nombre": self.nombreConductor,
            "Rut": self.rut,
            "Patente": self.patenteVehiculo,
            "tiempo": self.duracion,
            "valor": self.precio,
        }
        ticket_json = json.dumps(ticket_aux)
        os.makedirs("Boletas", exist_ok=True)
        file_path = os.path.join("Boletas", "ticket.json")
        with open(file_path, "w") as json_file:
            json_file.write(ticket_json)
