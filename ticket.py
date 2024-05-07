import json
class ticket:
    
    nombreConductor: str
    patenteVehiculo: str
    duracion: str
    precio: str
    rut: str
    
    def __init__(self, nombreConductor, patenteVehiculo, duracion, precio, rut):
        
        self.nombreConductor = nombreConductor
        self.patenteVehiculo = patenteVehiculo
        self.duracion = duracion
        self.precio = precio
        self.rut = rut
        #aca tendria que ir el lugar en la amtriz que falta hacer aun
        
    def Crear_Boleta(){
        ticket_aux = {
            "Rut": ticket.rut,
            "Nombre": ticket.nombre,
            "Patente": ticket.patenteVehiculo,
            "tiempo": ticket.duracion,
            "valor": ticket.precio,
            #"lugar": ticket.lugar porque la matriz aun no esta hecha
        }
        ticket_json = json.dumps(ticket_aux)
        with open("ticket.json", "w") as json_file:
            json_file.write(ticket_json)
    }
    #preguntar al profe si en la funcion open es mejor el "w" o el "a" o el "r+" no se cual estaria mejor
#preguntar igual una forma de que las boletas vallan guardandose con distintos numeros o si el mismo explorador de archivos va creando
#distintos numeros en los ticket(como cuando hay un mismo archivo el ordenador hace archivo archivo(2)
