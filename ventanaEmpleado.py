from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_empleado(QtWidgets.QDialog):
    
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
        self.btnIniciar.setText("Iniciar seción")
        self.btnAtras.setText("Atrás")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    empleado = Ui_empleado()
    ui = Ui_empleado()
    ui.setupEmpleado(empleado)
    empleado.show()
    sys.exit(app.exec())
