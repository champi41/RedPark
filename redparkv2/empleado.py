class empleado:
    
    nombre = str
    rut: str
    correo: str
    telefono: int
    contraseña: str
    
    def __init__(self, nombre, rut, correo, telefono, contraseña):
        
        self.nombre = nombre
        self.rut = rut
        self.correo = correo
        self.telefono = telefono
        self.contraseña = contraseña
        
    def iniciar_sesion(self):
        
        pass
    
    