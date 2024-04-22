class cliente:
    nombre : str
    apellido : str
    telefono : int
    correo : str
    rut : str
    def __init__(self, nombre, apellido, telefono, correo, rut,):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.rut = rut
    @classmethod
    def crear_cliente(cls):
        nombre = input("Ingrese el nombre del cliente: ")
        apellido = input("Ingrese el apellido del cliente: ")
        rut = input("Ingrese el RUT del cliente: ")
        telefono = input("Ingrese el teléfono del cliente: ")
        correo = input("Ingrese el correo electrónico del cliente: ")
        return cls(nombre, apellido, rut, telefono, correo)
    def mostrar_cliente(self):
        print("Información del cliente:")
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("RUT:", self.rut)
        print("Teléfono:", self.telefono)
        print("Correo electrónico:", self.correo)
nuevo_cliente = cliente.crear_cliente()
nuevo_cliente.mostrar_cliente()