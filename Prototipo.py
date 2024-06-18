import json
import os

BaseDato = "BaseDato.json"
if not os.path.exists(BaseDato):
    with open(BaseDato, 'w') as ArchivodeDatos:
        json.dump({}, ArchivodeDatos)
        
def LeerBD():
    with open(BaseDato, 'r') as ArchivodeDatos:
        return json.load(ArchivodeDatos)

def EscribirBD(data):
    with open(BaseDato, 'w') as ArchivodeDatos:
        json.dump(data, ArchivodeDatos, indent=4)
        
def LeerTodo():
    return LeerBD()

def Crear_Actualizar(key, value):
    data = LeerBD()
    data[key] = value
    EscribirBD(data)

def LeerArchivo(key):
    data = LeerBD()
    return data.get(key, None)


Crear_Actualizar('1', {'Nombre': 'Alice', 'Edad': 30})
Crear_Actualizar('2', {'Nombre': 'Bob', 'Edad': 25})

print(LeerArchivo('1'))