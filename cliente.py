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
    def crear_cliente(self, nombre, apellido, telefono, correo, rut,):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.rut = rut
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        telefono = input("Ingrese su telefono: ")
        correo = input("Ingrese su correo: ")
        rut = input("Ingrese su rut: ")
        print("Nombre: ", nombre)
        print("Apellido: ", apellido)


        
    
    
    
    