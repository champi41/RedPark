from PyQt6 import QtCore, QtGui, QtWidgets
import json
import os

BaseDato = "BaseDato.json"
if not os.path.exists(BaseDato):
    with open(BaseDato, 'w') as ArchivodeDatos:
        json.dump({}, ArchivodeDatos)

class Ui_empleado(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

    def LeerBD(self):
        with open(BaseDato, 'r') as ArchivodeDatos:
            return json.load(ArchivodeDatos)

    def EscribirBD(self, data):
        with open(BaseDato, 'w') as ArchivodeDatos:
            json.dump(data, ArchivodeDatos, indent=4)

    def LeerTodo(self):
        return self.LeerBD()

    def LeerArchivo(self, key):
        data = self.LeerBD()
        return data.get(key, None)

    def Crear_Actualizar(self, key, value):
        data = self.LeerBD()
        data[key] = value
        self.EscribirBD(data)

    def setupEmpleado(self, empleado):
        empleado.setObjectName("empleado")
        empleado.resize(640, 480)
        empleado.setStyleSheet("background-color: rgb(0, 0, 90);\n"
"color: rgb(255, 255, 255);")
        self.lblEmpleado = QtWidgets.QLabel(parent=empleado)
        self.lblEmpleado.setGeometry(QtCore.QRect(160, 50, 320, 50))
        self.lblEmpleado.setObjectName("lblEmpleado")
        self.inptNombre = QtWidgets.QLineEdit(parent=empleado)
        self.inptNombre.setGeometry(QtCore.QRect(170, 180, 300, 30))
        self.inptNombre.setObjectName("inptNombre")
        self.inptContrasena = QtWidgets.QLineEdit(parent=empleado)
        self.inptContrasena.setGeometry(QtCore.QRect(170, 260, 300, 30))
        self.inptContrasena.setObjectName("inptContrasena")
        self.lblNombre = QtWidgets.QLabel(parent=empleado)
        self.lblNombre.setGeometry(QtCore.QRect(170, 150, 240, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lblNombre.setFont(font)
        self.lblNombre.setObjectName("lblNombre")
        self.lblContrsena = QtWidgets.QLabel(parent=empleado)
        self.lblContrsena.setGeometry(QtCore.QRect(170, 230, 240, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lblContrsena.setFont(font)
        self.lblContrsena.setObjectName("lblContrsena")
        self.btnRegistrar = QtWidgets.QPushButton(parent=empleado)
        self.btnRegistrar.setGeometry(QtCore.QRect(260, 320, 121, 41))
        self.btnRegistrar.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"border-radius: 20px;\n"
"")
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.btnIniciar = QtWidgets.QPushButton(parent=empleado)
        self.btnIniciar.setGeometry(QtCore.QRect(260, 380, 121, 41))
        self.btnIniciar.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"border-radius: 20px;")
        self.btnIniciar.setObjectName("btnIniciar")
        self.btnAtras = QtWidgets.QPushButton(parent=empleado)
        self.btnAtras.setGeometry(QtCore.QRect(20, 423, 111, 41))
        self.btnAtras.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"border-radius: 20px;\n"
"")
        self.btnAtras.setObjectName("btnAtras")

        empleado.setWindowTitle("Empleado")
        self.lblEmpleado.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Registro empleado</span></p></body></html>")
        self.lblNombre.setText("<html><head/><body><p><span style=\" font-size:14pt;\">Nombre del empleado</span></p></body></html>")
        self.lblContrsena.setText("<html><head/><body><p>Contraseña</p><p><br/></p></body></html>")
        self.btnRegistrar.setText("Registrarse")
        self.btnIniciar.setText("Iniciar sesión")
        self.btnAtras.setText("Atrás")
        self.btnRegistrar.clicked.connect(self.registrarEmpleado)

    def registrarEmpleado(self):
        nombre = self.inptNombre.text()
        contrasena = self.inptContrasena.text()
        if nombre and contrasena:
            self.Crear_Actualizar(nombre, {"Nombre": nombre, "Contrasena": contrasena})
            QtWidgets.QMessageBox.information(self, "Éxito", "Empleado registrado correctamente")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor, complete todos los campos")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    empleado = QtWidgets.QDialog()
    ui = Ui_empleado()
    ui.setupEmpleado(empleado)
    empleado.show()
    sys.exit(app.exec())