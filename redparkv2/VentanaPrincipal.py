from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QFileDialog, QLineEdit
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl
import json
import os
from datetime import datetime 

class Ui_VentanaPrincipal(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setObjectName("VentanaPrincipal")
        self.resize(640, 480)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(22)
        self.setFont(font)
        self.setStyleSheet("background-color: rgb(0, 0, 90);\n""color: rgb(255, 255, 255);\n")
        
        self.redPark = QtWidgets.QWidget(parent=self)
        self.redPark.setObjectName("centralwidget")
        self.setCentralWidget(self.redPark)
        
        self.setupUi()
        
    def setupUi(self):
        self.lblRedBank = QtWidgets.QLabel(parent=self.redPark)
        self.lblRedBank.setGeometry(QtCore.QRect(135, 80, 370, 120))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(50)
        self.lblRedBank.setFont(font)
        self.lblRedBank.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblRedBank.setObjectName("lblRedBank")
        self.lblRedBank.setText("<html><head/><body><p><span style=\" font-size:72pt; font-style:italic; color:#ffffff;\">Red</span><span style=\" font-size:72pt; font-weight:700; color:#ff0004;\">Park</span></p></body></html>")

        self.btnTicket = QtWidgets.QPushButton(parent=self.redPark)
        self.btnTicket.setGeometry(QtCore.QRect(225, 240, 190, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnTicket.setFont(font)
        self.btnTicket.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnTicket.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.btnTicket.setObjectName("btnTicket")
        self.btnTicket.setText("Iniciar")
        self.btnTicket.clicked.connect(self.showRegistro)
        
        self.btnEmpleado = QtWidgets.QPushButton(parent=self.redPark)
        self.btnEmpleado.setGeometry(QtCore.QRect(20, 425, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnEmpleado.setFont(font)
        self.btnEmpleado.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnEmpleado.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.btnEmpleado.setObjectName("btnEmpleado")
        self.btnEmpleado.setText("Empleado")
        self.btnEmpleado.clicked.connect(self.showEmpleado)
        
        self.registro = Registro(self)
        self.registro.hide()
        
        self.matriz = Matriz(self)
        self.matriz.hide()
        
        self.duracion = Duracion(self)
        self.duracion.hide()
        
        self.redticket = RedTicket(self)
        self.redticket.hide()
        
        self.ventanaEmpleado = Ui_empleado(self)
        self.ventanaEmpleado.hide()
        
        self.resumen = Ui_Resumen(self)
        self.resumen.hide()
        
    def showRegistro(self):
        self.redPark.hide()
        self.registro.show()
        self.registro.limpiar()
        
    def mostrarMatriz(self):
        self.duracion.hide()
        self.matriz.show()
        
    def showMatriz(self):
        self.registro.hide()
        self.matriz.show()

    def atrasMatriz(self):
        self.matriz.hide()
        self.registro.show()

    def showDuracion(self):
        self.matriz.hide()
        self.registro.hide()
        self.duracion.show()
        
    def atrasDuracion(self):
        self.redticket.hide()
        self.duracion.show()
        
    def showRedTicket(self,boton, nombre="", patente=""):
        self.matriz.hide()
        self.duracion.hide()
        nombre = self.registro.inptNombre.text()
        patente = self.registro.inptPatente.text()
        self.redticket.setupRedTicket(nombre, patente, boton)
        self.redticket.show()
        
    def retornar(self):
        self.redticket.hide()
        self.redPark.show()
    
    def ventanaPrincipal(self):
        self.redPark.show()
        self.registro.hide()
        self.ventanaEmpleado.hide()
        
    def showEmpleado(self):
        self.resumen.hide()
        self.duracion.hide()
        self.redPark.hide()
        self.ventanaEmpleado.show()
        self.ventanaEmpleado.limpiar()
        
    def showResumen(self, usuario):
        self.resumen.setUsuario(usuario)
        self.ventanaEmpleado.hide()
        self.resumen.show()
class Registro(QtWidgets.QWidget):
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.setupRegistro()
        
    def setupRegistro(self):
        
        self.setObjectName("registro")
        self.resize(640, 480)
        self.setStyleSheet("background-color: rgb(0, 0, 90);\n""color: rgb(255, 255, 255);\n""")
        self.setWindowTitle("Registro RedPark")
        
        self.lblRegistro = QtWidgets.QLabel(parent=self)
        self.lblRegistro.setGeometry(QtCore.QRect(10, 60, 620, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        self.lblRegistro.setFont(font)
        self.lblRegistro.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblRegistro.setObjectName("lblRegistro")
        
        self.inptNombre = QtWidgets.QLineEdit(parent=self)
        self.inptNombre.setGeometry(QtCore.QRect(170, 200, 300, 30))
        self.inptNombre.setObjectName("inptNombre")
        
        regex1 = QRegularExpression("^[a-zA-Z ]*$")  # Permitir solo letras y espacios
        validator1 = QRegularExpressionValidator(regex1, self.inptNombre)

        # Asignar el validador al QLineEdit
        self.inptNombre.setValidator(validator1)
        
        self.inptPatente = QtWidgets.QLineEdit(parent=self)
        self.inptPatente.setGeometry(QtCore.QRect(170, 280, 300, 30))
        self.inptPatente.setObjectName("inptPatente")
        self.inptPatente.setMaxLength(6)
        
        regex2 = QRegularExpression("^[A-Za-z0-9]*$")  # Permitir letras mayúsculas y minúsculas y números
        validator2 = QRegularExpressionValidator(regex2, self.inptPatente)

        # Asignar el validador al QLineEdit
        self.inptPatente.setValidator(validator2)
        
        self.lblNomCon = QtWidgets.QLabel(parent=self)
        self.lblNomCon.setGeometry(QtCore.QRect(170, 170, 240, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lblNomCon.setFont(font)
        self.lblNomCon.setObjectName("lblNomCon")
        
        self.lblPatente = QtWidgets.QLabel(parent=self)
        self.lblPatente.setGeometry(QtCore.QRect(170, 250, 240, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lblPatente.setFont(font)
        self.lblPatente.setObjectName("lblPatente")
        
        self.btnIngresar = QtWidgets.QPushButton(parent=self)
        self.btnIngresar.setGeometry(QtCore.QRect(475, 425, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btnIngresar.setFont(font)
        self.btnIngresar.setStyleSheet("border-radius: 20px;\n""background-color: rgb(255, 0, 4);\n""")
        self.btnIngresar.setObjectName("btnIngresar")
        self.btnIngresar.clicked.connect(self.parent().showMatriz)

        self.inptNombre.textChanged.connect(self.validarEntradas)
        self.inptPatente.textChanged.connect(self.validarEntradas)

        self.validarEntradas()
        
        self.btnAtras = QtWidgets.QPushButton(parent=self)
        self.btnAtras.setGeometry(QtCore.QRect(20, 425, 150, 40))
        self.btnAtras.setFont(font)
        self.btnAtras.setStyleSheet("border-radius: 20px;\n""background-color: rgb(255, 0, 4);\n""")
        self.btnAtras.setObjectName("btnAtras")
        self.btnAtras.setText("Atrás")
        self.btnAtras.clicked.connect(self.parent().ventanaPrincipal)

        self.lblRegistro.setText("Registro")
        self.lblNomCon.setText("Nombre del conductor")
        self.lblPatente.setText("Patente del vehículo")
        self.btnIngresar.setText("Ingresar")
    
    def limpiar(self):
        
        self.inptNombre.clear()
        self.inptPatente.clear()    
        
    def validarEntradas(self):

        nombre_valido = bool(self.inptNombre.text().strip())
        self.btnIngresar.setEnabled(nombre_valido)


class Duracion(QtWidgets.QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.setupDuracion()
        
    def setupDuracion(self):
        self.setObjectName("tiempo")
        self.resize(640, 480)
        self.setStyleSheet("background-color: rgb(0, 0, 90);\n"
"color: rgb(255, 255, 255);\n"
"")
        
        self.hora1btn = QtWidgets.QPushButton(parent=self)
        self.hora1btn.setGeometry(QtCore.QRect(280, 160, 80, 133))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        self.hora1btn.setFont(font)
        self.hora1btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.hora1btn.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.hora1btn.setObjectName("hora1btn")
        self.hora1btn.clicked.connect(lambda: self.parent().showRedTicket(1))
        
        self.min30btn = QtWidgets.QPushButton(parent=self)
        self.min30btn.setGeometry(QtCore.QRect(170, 160, 80, 133))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        self.min30btn.setFont(font)
        self.min30btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.min30btn.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.min30btn.setObjectName("min30btn")
        self.min30btn.clicked.connect(lambda: self.parent().showRedTicket(0.5))
        
        self.hora3btn = QtWidgets.QPushButton(parent=self)
        self.hora3btn.setGeometry(QtCore.QRect(500, 160, 80, 133))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        self.hora3btn.setFont(font)
        self.hora3btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.hora3btn.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.hora3btn.setObjectName("hora3btn")
        self.hora3btn.clicked.connect(lambda: self.parent().showRedTicket(3))
        
        self.lblSelecTiemp = QtWidgets.QLabel(parent=self)
        self.lblSelecTiemp.setGeometry(QtCore.QRect(10, 60, 620, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        self.lblSelecTiemp.setFont(font)
        self.lblSelecTiemp.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblSelecTiemp.setObjectName("label")
        
        self.hora2btn = QtWidgets.QPushButton(parent=self)
        self.hora2btn.setGeometry(QtCore.QRect(390, 160, 80, 133))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        self.hora2btn.setFont(font)
        self.hora2btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.hora2btn.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.hora2btn.setObjectName("hora2btn")
        self.hora2btn.clicked.connect(lambda: self.parent().showRedTicket(2))
        
        self.min15btn = QtWidgets.QPushButton(parent=self)
        self.min15btn.setGeometry(QtCore.QRect(60, 160, 80, 133))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        self.min15btn.setFont(font)
        self.min15btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.min15btn.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.min15btn.setObjectName("min15btn")
        self.min15btn.clicked.connect(lambda: self.parent().showRedTicket(0.25))
        
        self.lbl600 = QtWidgets.QLabel(parent=self)
        self.lbl600.setGeometry(QtCore.QRect(60, 310, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl600.setFont(font)
        self.lbl600.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl600.setObjectName("lbl600")
        
        self.lbl1050 = QtWidgets.QLabel(parent=self)
        self.lbl1050.setGeometry(QtCore.QRect(170, 310, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl1050.setFont(font)
        self.lbl1050.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl1050.setObjectName("lbl1050")
        
        self.lbl1800 = QtWidgets.QLabel(parent=self)
        self.lbl1800.setGeometry(QtCore.QRect(280, 310, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl1800.setFont(font)
        self.lbl1800.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl1800.setObjectName("lbl1800")
        
        self.lbl3000 = QtWidgets.QLabel(parent=self)
        self.lbl3000.setGeometry(QtCore.QRect(390, 310, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl3000.setFont(font)
        self.lbl3000.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl3000.setObjectName("lbl3000")
        
        self.lbl3600 = QtWidgets.QLabel(parent=self)
        self.lbl3600.setGeometry(QtCore.QRect(500, 310, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl3600.setFont(font)
        self.lbl3600.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl3600.setObjectName("lbl3600")
        
        self.btnAtras = QtWidgets.QPushButton(parent=self)
        self.btnAtras.setGeometry(QtCore.QRect(20, 425, 150, 40))
        font.setPointSize(12)
        self.btnAtras.setFont(font)
        self.btnAtras.setStyleSheet("border-radius: 20px;\n""background-color: rgb(255, 0, 4);\n""")
        self.btnAtras.setObjectName("btnAtras")
        self.btnAtras.setText("Atrás")
        self.btnAtras.clicked.connect(self.parent().mostrarMatriz)
        
        self.lblAviso = QtWidgets.QLabel(parent=self)
        self.lblAviso.setGeometry(QtCore.QRect(58, 360, 521, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lblAviso.setFont(font)
        self.lblAviso.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblAviso.setObjectName("lblAviso")
        
        self.lblSelecTiemp.setText("Seleccione el tiempo")
        self.min15btn.setText("15\n""Minutos")
        self.min30btn.setText("30\n""Minutos")
        self.hora1btn.setText("1\n""Hora")
        self.hora2btn.setText("2\n""Horas")
        self.hora3btn.setText("3\n""Horas")
        
        self.lbl600.setText("$450")
        self.lbl1050.setText("$900")
        self.lbl1800.setText("$1800")
        self.lbl3000.setText("$3600")
        self.lbl3600.setText("$5400")
        self.lblAviso.setText("Si excede el tiempo que ingresó, se le cobrará $45 por cada minuto excedido.")
        
class Matriz(QtWidgets.QWidget):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.checkboxes = {}
        self.setupMatriz()
        
    def setupMatriz(self):
        
        self.setObjectName("Dialog")
        self.resize(640, 480)
        self.setStyleSheet("background-color: rgb(0, 0, 90);\n"
"color: rgb(255, 255, 255);")
        
        self.lblLugar = QtWidgets.QLabel(parent=self)
        self.lblLugar.setGeometry(QtCore.QRect(160, 50, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        self.lblLugar.setFont(font)
        self.lblLugar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblLugar.setObjectName("lblLugar")
        
        self.btnSiguiente = QtWidgets.QPushButton(parent=self)
        font.setPointSize(12)
        self.btnSiguiente.setFont(font)
        self.btnSiguiente.setGeometry(QtCore.QRect(475, 425, 150, 40))
        self.btnSiguiente.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 20px\n"
"")
        
        self.btnSiguiente.clicked.connect(self.parent().showDuracion)
        self.btnSiguiente.clicked.connect(self.confirmar_checkbox)
        self.btnSiguiente.setObjectName("btnSiguiente")
        
        self.btnAtras = QtWidgets.QPushButton(parent=self)
        font.setPointSize(12)
        self.btnAtras.setFont(font)
        self.btnAtras.setGeometry(QtCore.QRect(20, 425, 150, 40))
        self.btnAtras.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 20px\n"
"")      
        self.btnAtras.clicked.connect(self.parent().atrasMatriz)
        self.btnAtras.setObjectName("btnAtras")
        
        self.A1 = QtWidgets.QCheckBox(parent=self)
        self.A1.setGeometry(QtCore.QRect(120, 150, 76, 20))
        self.A1.setObjectName("A1")
        self.B1 = QtWidgets.QCheckBox(parent=self)
        self.B1.setGeometry(QtCore.QRect(210, 150, 76, 20))
        self.B1.setObjectName("B1")
        self.C1 = QtWidgets.QCheckBox(parent=self)
        self.C1.setGeometry(QtCore.QRect(300, 150, 76, 20))
        self.C1.setObjectName("C1")
        self.D1 = QtWidgets.QCheckBox(parent=self)
        self.D1.setGeometry(QtCore.QRect(390, 150, 76, 20))
        self.D1.setObjectName("D1")
        self.E1 = QtWidgets.QCheckBox(parent=self)
        self.E1.setGeometry(QtCore.QRect(480, 150, 76, 20))
        self.E1.setObjectName("E1")
        self.B2 = QtWidgets.QCheckBox(parent=self)
        self.B2.setGeometry(QtCore.QRect(210, 180, 76, 20))
        self.B2.setObjectName("B2")
        self.C2 = QtWidgets.QCheckBox(parent=self)
        self.C2.setGeometry(QtCore.QRect(300, 180, 76, 20))
        self.C2.setObjectName("C2")
        self.A2 = QtWidgets.QCheckBox(parent=self)
        self.A2.setGeometry(QtCore.QRect(120, 180, 76, 20))
        self.A2.setObjectName("A2")
        self.D2 = QtWidgets.QCheckBox(parent=self)
        self.D2.setGeometry(QtCore.QRect(390, 180, 76, 20))
        self.D2.setObjectName("D2")
        self.E2 = QtWidgets.QCheckBox(parent=self)
        self.E2.setGeometry(QtCore.QRect(480, 180, 76, 20))
        self.E2.setObjectName("E2")
        self.B3 = QtWidgets.QCheckBox(parent=self)
        self.B3.setGeometry(QtCore.QRect(210, 210, 76, 20))
        self.B3.setObjectName("B3")
        self.C3 = QtWidgets.QCheckBox(parent=self)
        self.C3.setGeometry(QtCore.QRect(300, 210, 76, 20))
        self.C3.setObjectName("C3")
        self.A3 = QtWidgets.QCheckBox(parent=self)
        self.A3.setGeometry(QtCore.QRect(120, 210, 76, 20))
        self.A3.setObjectName("A3")
        self.D3 = QtWidgets.QCheckBox(parent=self)
        self.D3.setGeometry(QtCore.QRect(390, 210, 76, 20))
        self.D3.setObjectName("D3")
        self.E3 = QtWidgets.QCheckBox(parent=self)
        self.E3.setGeometry(QtCore.QRect(480, 210, 76, 20))
        self.E3.setObjectName("E3")
        self.B4 = QtWidgets.QCheckBox(parent=self)
        self.B4.setGeometry(QtCore.QRect(210, 240, 76, 20))
        self.B4.setObjectName("B4")
        self.C4 = QtWidgets.QCheckBox(parent=self)
        self.C4.setGeometry(QtCore.QRect(300, 240, 76, 20))
        self.C4.setObjectName("C4")
        self.A4 = QtWidgets.QCheckBox(parent=self)
        self.A4.setGeometry(QtCore.QRect(120, 240, 76, 20))
        self.A4.setObjectName("A4")
        self.D4 = QtWidgets.QCheckBox(parent=self)
        self.D4.setGeometry(QtCore.QRect(390, 240, 76, 20))
        self.D4.setObjectName("D4")
        self.E4 = QtWidgets.QCheckBox(parent=self)
        self.E4.setGeometry(QtCore.QRect(480, 240, 76, 20))
        self.E4.setObjectName("E4")
        self.B5 = QtWidgets.QCheckBox(parent=self)
        self.B5.setGeometry(QtCore.QRect(210, 270, 76, 20))
        self.B5.setObjectName("B5")
        self.C5 = QtWidgets.QCheckBox(parent=self)
        self.C5.setGeometry(QtCore.QRect(300, 270, 76, 20))
        self.C5.setObjectName("C5")
        self.A5 = QtWidgets.QCheckBox(parent=self)
        self.A5.setGeometry(QtCore.QRect(120, 270, 76, 20))
        self.A5.setObjectName("A5")
        self.D5 = QtWidgets.QCheckBox(parent=self)
        self.D5.setGeometry(QtCore.QRect(390, 270, 76, 20))
        self.D5.setObjectName("D5")
        self.E5 = QtWidgets.QCheckBox(parent=self)
        self.E5.setGeometry(QtCore.QRect(480, 270, 76, 20))
        self.E5.setObjectName("E5")
        self.B6 = QtWidgets.QCheckBox(parent=self)
        self.B6.setGeometry(QtCore.QRect(210, 300, 76, 20))
        self.B6.setObjectName("B6")
        self.C6 = QtWidgets.QCheckBox(parent=self)
        self.C6.setGeometry(QtCore.QRect(300, 300, 76, 20))
        self.C6.setObjectName("C6")
        self.A6 = QtWidgets.QCheckBox(parent=self)
        self.A6.setGeometry(QtCore.QRect(120, 300, 76, 20))
        self.A6.setObjectName("A6")
        self.D6 = QtWidgets.QCheckBox(parent=self)
        self.D6.setGeometry(QtCore.QRect(390, 300, 76, 20))
        self.D6.setObjectName("D6")
        self.E6 = QtWidgets.QCheckBox(parent=self)
        self.E6.setGeometry(QtCore.QRect(480, 300, 76, 20))
        self.E6.setObjectName("E6")
        self.B7 = QtWidgets.QCheckBox(parent=self)
        self.B7.setGeometry(QtCore.QRect(210, 330, 76, 20))
        self.B7.setObjectName("B7")
        self.C7 = QtWidgets.QCheckBox(parent=self)
        self.C7.setGeometry(QtCore.QRect(300, 330, 76, 20))
        self.C7.setObjectName("C7")
        self.A7 = QtWidgets.QCheckBox(parent=self)
        self.A7.setGeometry(QtCore.QRect(120, 330, 76, 20))
        self.A7.setObjectName("A7")
        self.D7 = QtWidgets.QCheckBox(parent=self)
        self.D7.setGeometry(QtCore.QRect(390, 330, 76, 20))
        self.D7.setObjectName("D7")
        self.E7 = QtWidgets.QCheckBox(parent=self)
        self.E7.setGeometry(QtCore.QRect(480, 330, 76, 20))
        self.E7.setObjectName("E7")

        self.setWindowTitle("Dialog")
        self.lblLugar.setText("Seleccione su lugar")
        self.btnSiguiente.setText("Siguiente")
        self.btnAtras.setText("Atrás")
        self.A1.setText("A1")
        self.B1.setText("B1")
        self.C1.setText("C1")
        self.D1.setText("D1")
        self.E1.setText("E1")
        self.B2.setText("B2")
        self.C2.setText("C2")
        self.A2.setText("A2")
        self.D2.setText("D2")
        self.E2.setText("E2")
        self.B3.setText("B3")
        self.C3.setText("C3")
        self.A3.setText("A3")
        self.D3.setText("D3")
        self.E3.setText("E3")
        self.B4.setText("B4")
        self.C4.setText("C4")
        self.A4.setText("A4")
        self.D4.setText("D4")
        self.E4.setText("E4")
        self.B5.setText("B5")
        self.C5.setText("C5")
        self.A5.setText("A5")
        self.D5.setText("D5")
        self.E5.setText("E5")
        self.B6.setText("B6")
        self.C6.setText("C6")
        self.A6.setText("A6")
        self.D6.setText("D6")
        self.E6.setText("E6")
        self.B7.setText("B7")
        self.C7.setText("C7")
        self.A7.setText("A7")
        self.D7.setText("D7")
        self.E7.setText("E7")        
        
        self.grupo_botones = QtWidgets.QButtonGroup(self)
        self.grupo_botones.setExclusive(True)
        
        checkboxes = [
            self.A1, self.B1, self.C1, self.D1, self.E1,
            self.A2, self.B2, self.C2, self.D2, self.E2,
            self.A3, self.B3, self.C3, self.D3, self.E3,
            self.A4, self.B4, self.C4, self.D4, self.E4,
            self.A5, self.B5, self.C5, self.D5, self.E5,
            self.A6, self.B6, self.C6, self.D6, self.E6,
            self.A7, self.B7, self.C7, self.D7, self.E7
        ]
        
        for checkbox in checkboxes:
            self.grupo_botones.addButton(checkbox)
            self.checkboxes[checkbox.objectName()] = checkbox  # Agregar al diccionario
        
    def confirmar_checkbox(self):
        for checkbox in self.checkboxes.values():
            if checkbox.isChecked():
                self.parent().selected_spot = checkbox.objectName()
                checkbox.setEnabled(False)
                self.parent().showDuracion()
                break
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor, seleccione un lugar.")  
    def limpiar(self):
        checkboxes = [self.A1, self.B1, self.C1, self.D1, self.E1, self.A2, self.B2, self.C2, self.D2, self.E2,
                      self.A3, self.B3, self.C3, self.D3, self.E3, self.A4, self.B4, self.C4, self.D4, self.E4,
                      self.A5, self.B5, self.C5, self.D5, self.E5]
        for checkbox in checkboxes:
            checkbox.setChecked(False)
class RedTicket(QtWidgets.QWidget):
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.setupRedTicket( nombre="", patente="",)
   
    def Crear_Boleta(self, boton):

        timestamp = datetime.now().strftime("%H, %M, %S, %d, %m, %Y")
        file_name = f"ticket_{timestamp}.json"
        checked_names = []
        for checkbox in self.parent().matriz.checkboxes.values():
            if checkbox.isChecked():
                checked_names.append(checkbox.objectName())
        checkbox_names = ", ".join(checked_names)
        ticket_aux = {
            "Nombre":  self.parent().registro.inptNombre.text(),
            "Patente":  self.parent().registro.inptPatente.text(),
            "Puesto" : checkbox_names,
            "Duracion": str(boton) + "hrs",
            "Precio": boton * 1800
        }
        ticket_json = json.dumps(ticket_aux)
        os.makedirs("Boletas", exist_ok=True)
        file_path = os.path.join("Boletas", file_name)
        with open(file_path, "w") as json_file:
            json_file.write(ticket_json)

    def new_method(self):
        ticket_aux = self.ticket
    def setupRedTicket(self, nombre, patente, boton=0):
        
        self.setObjectName("redticket")
        self.resize(640, 480)
        self.setStyleSheet("background-color: rgb(0, 0, 90);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.setWindowTitle("RedTicket")
        
        self.lblTicket = QtWidgets.QLabel(parent=self)
        self.lblTicket.setGeometry(QtCore.QRect(170, 50, 300, 91))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        self.lblTicket.setFont(font)
        self.lblTicket.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblTicket.setObjectName("lblTicket")
        
        self.lblNombre = QtWidgets.QLabel(parent=self)
        self.lblNombre.setGeometry(QtCore.QRect(90, 200, 320, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lblNombre.setFont(font)
        self.lblNombre.setObjectName("lblNombre")
        
        self.lblPatente = QtWidgets.QLabel(parent=self)
        self.lblPatente.setGeometry(QtCore.QRect(90, 240, 320, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lblPatente.setFont(font)
        self.lblPatente.setObjectName("lblPatente")
        
        self.lblPuesto= QtWidgets.QLabel(parent=self)
        self.lblPuesto.setGeometry(QtCore.QRect(90, 280, 240, 21))
        font= QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lblPuesto.setFont(font)
        self.lblPuesto.setObjectName("lblPuesto")
        
        self.lblDuracion = QtWidgets.QLabel(parent=self)
        self.lblDuracion.setGeometry(QtCore.QRect(90, 320, 240, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lblDuracion.setFont(font)
        self.lblDuracion.setObjectName("lblDuracion")
        
        self.btnGuardarTicket = QtWidgets.QPushButton(parent=self)
        self.btnGuardarTicket.setGeometry(QtCore.QRect(250, 400, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        
        self.btnGuardarTicket.setText("Guardar Ticket")
        self.btnGuardarTicket.setFont(font)
        self.btnGuardarTicket.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnGuardarTicket.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(255, 0, 4);\n"
"")
        self.btnGuardarTicket.setObjectName("btnGuardarTicket")
        self.btnGuardarTicket.clicked.connect(self.parent().retornar)
        self.btnGuardarTicket.clicked.connect(lambda: self.Crear_Boleta(boton))
        
        self.btnAtras = QtWidgets.QPushButton(parent=self)
        self.btnAtras.setGeometry(QtCore.QRect(20, 425, 150, 40))
        self.btnAtras.setFont(font)
        self.btnAtras.setStyleSheet("border-radius: 20px;\n""background-color: rgb(255, 0, 4);\n""")
        self.btnAtras.setObjectName("btnAtras")
        self.btnAtras.setText("Atrás")
        self.btnAtras.clicked.connect(self.parent().atrasDuracion)
        
        self.lblTicket.setText("RedTicket")
        self.lblNombre.setText("Nombre del conductor: " + self.parent().registro.inptNombre.text())
        self.lblPatente.setText("Patente del vehiculo: " + self.parent().registro.inptPatente.text())
        checked_names = []
        for checkbox in self.parent().matriz.checkboxes.values():
            if checkbox.isChecked():
                checked_names.append(checkbox.objectName())
        checkbox_names = ", ".join(checked_names)
        self.lblPuesto.setText("Puesto: " + checkbox_names)
        self.lblDuracion.setText("Duración del Ticket: " + str(boton) + " horas")
        
        precio_total = boton * 1800
        
        self.lblPrecio = QtWidgets.QLabel(parent=self)
        self.lblPrecio.setGeometry(QtCore.QRect(90, 360, 240, 21))
        font.setPointSize(14)
        self.lblPrecio.setFont(font)
        self.lblPrecio.setObjectName("lblPrecio")
        self.lblPrecio.setText("Precio: $" + str(precio_total))

BaseDato = "BaseDato.json"
if not os.path.exists(BaseDato):
    with open(BaseDato, 'w') as ArchivodeDatos:
        json.dump({}, ArchivodeDatos)

class Ui_empleado(QtWidgets.QWidget):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.setupEmpleado(usuario="")
        
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

    def registrar_usuario(self, usuario, datos_usuario):
        data = self.LeerBD()
        if usuario in data:
            return False
        data[usuario] = datos_usuario
        self.EscribirBD(data)
        return True

    def iniciar_sesion_usuario(self, usuario, contrasena):
        data = self.LeerBD()
        if usuario in data and data[usuario]["Contrasena"] == contrasena:
            return True
        return False

    def usuario_existente(self, usuario):
        data = self.LeerBD()
        return usuario in data
    
    def setupEmpleado(self, usuario):
        self.setObjectName("self")
        self.resize(640, 480)
        self.setStyleSheet("background-color: rgb(0, 0, 90);\n"
"color: rgb(255, 255, 255);")
        self.lblEmpleado = QtWidgets.QLabel(parent=self)
        self.lblEmpleado.setGeometry(QtCore.QRect(160, 50, 320, 50))
        self.lblEmpleado.setObjectName("lblEmpleado")
        
        self.inptNombre = QtWidgets.QLineEdit(parent=self)
        self.inptNombre.setGeometry(QtCore.QRect(170, 180, 300, 30))
        self.inptNombre.setObjectName("inptNombre")
        
        regex3 = QRegularExpression("^[A-Za-z]*$")  # Permitir letras mayúsculas y minúsculas
        validator3 = QRegularExpressionValidator(regex3, self.inptNombre)

        # Asignar el validador al QLineEdit
        self.inptNombre.setValidator(validator3)
        
        self.inptContrasena = QtWidgets.QLineEdit(parent=self)
        self.inptContrasena.setGeometry(QtCore.QRect(170, 260, 300, 30))
        self.inptContrasena.setObjectName("inptContrasena")
        self.inptContrasena.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.lblNombre = QtWidgets.QLabel(parent=self)
        self.lblNombre.setGeometry(QtCore.QRect(170, 150, 240, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lblNombre.setFont(font)
        self.lblNombre.setObjectName("lblNombre")
        self.lblContrsena = QtWidgets.QLabel(parent=self)
        self.lblContrsena.setGeometry(QtCore.QRect(170, 230, 240, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lblContrsena.setFont(font)
        self.lblContrsena.setObjectName("lblContrsena")
        self.btnRegistrar = QtWidgets.QPushButton(parent=self)
        self.btnRegistrar.setGeometry(QtCore.QRect(260, 320, 121, 41))
        self.btnRegistrar.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"border-radius: 20px;\n"
"")
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.btnIniciar = QtWidgets.QPushButton(parent=self)
        self.btnIniciar.setGeometry(QtCore.QRect(260, 380, 121, 41))
        self.btnIniciar.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"border-radius: 20px;")
        self.btnIniciar.setObjectName("btnIniciar")
        
        self.btnAtras = QtWidgets.QPushButton(parent=self)
        font.setPointSize(12)
        self.btnAtras.setFont(font)
        self.btnAtras.setGeometry(QtCore.QRect(20, 425, 150, 40))
        self.btnAtras.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"border-radius: 20px;\n"
"")
        self.btnAtras.setObjectName("btnAtras")
        self.btnAtras.clicked.connect(self.parent().ventanaPrincipal)

        self.setWindowTitle("Empleado")
        self.lblEmpleado.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Registro empleado</span></p></body></html>")
        self.lblNombre.setText("<html><head/><body><p><span style=\" font-size:14pt;\">Nombre del empleado</span></p></body></html>")
        self.lblContrsena.setText("<html><head/><body><p>Contraseña</p><p><br/></p></body></html>")
        self.btnRegistrar.setText("Registrarse")
        self.btnIniciar.setText("Iniciar sesión")
        self.btnAtras.setText("Atrás")
        self.btnRegistrar.clicked.connect(self.registrarEmpleado)
        self.btnIniciar.clicked.connect(self.iniciarSesionEmpleado)
        
    def registrarEmpleado(self):
        nombre = self.inptNombre.text()
        contrasena = self.inptContrasena.text()
        if nombre and contrasena:
            if self.registrar_usuario(nombre, {"Nombre": nombre, "Contrasena": contrasena}):
                QtWidgets.QMessageBox.information(self, "Éxito", "Empleado registrado correctamente")
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "El usuario ya existe")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor, complete todos los campos")

    def iniciarSesionEmpleado(self):
        nombre = self.inptNombre.text()
        contrasena = self.inptContrasena.text()
        if nombre and contrasena:
            if self.iniciar_sesion_usuario(nombre, contrasena):
                QtWidgets.QMessageBox.information(self, "Éxito", "Inicio de sesión completado")
                self.parent().showResumen(nombre)  # Solo mostrar el resumen si el inicio de sesión es exitoso
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Usuario o credenciales incorrectas")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Por favor, complete todos los campos")
    def limpiar(self):
        self.inptNombre.clear()
        self.inptContrasena.clear()   
              
class Ui_Resumen(QtWidgets.QWidget):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.usuario = ""
        self.setupResumen()

    def setupResumen(self):
        self.setObjectName("Resumen")
        self.resize(640, 480)
        self.setStyleSheet("background-color: rgb(0, 0, 90);\n"
                              "color: rgb(255, 255, 255);")
        self.lblResumen = QtWidgets.QLabel(parent=self)
        self.lblResumen.setGeometry(QtCore.QRect(160, 50, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        self.lblResumen.setFont(font)
        self.lblResumen.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblResumen.setObjectName("lblResumen")

        self.lblUsuario = QtWidgets.QLabel(parent=self)
        self.lblUsuario.setGeometry(QtCore.QRect(160, 100, 320, 50))
        font.setPointSize(14)
        self.lblUsuario.setFont(font)
        self.lblUsuario.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblUsuario.setObjectName("lblUsuario")

        self.btnAtras = QtWidgets.QPushButton(parent=self)
        font.setPointSize(12)
        self.btnAtras.setFont(font)
        self.btnAtras.setGeometry(QtCore.QRect(20, 425, 150, 40))
        self.btnAtras.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                    "border-radius: 20px\n"
                                    "")
        self.btnAtras.setObjectName("btnAtras")
        self.btnAtras.clicked.connect(self.parent().showEmpleado)
        
        self.btnAbrirRes = QtWidgets.QPushButton(parent=self)
        self.btnAbrirRes.setGeometry(QtCore.QRect(220, 230, 201, 51))
        font.setPointSize(14)
        self.btnAbrirRes.setFont(font)
        self.btnAbrirRes.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                       "border-radius: 20px\n"
                                       "")
        self.btnAbrirRes.setObjectName("btnAbrirRes")
        self.btnAbrirRes.clicked.connect(self.abrir_boletas)

        self.setWindowTitle("Resumen")
        self.lblResumen.setText("Resumen de ventas")
        self.lblUsuario.setText(f"Usuario: {self.usuario}")
        self.btnAtras.setText("Atrás")
        self.btnAbrirRes.setText("Abrir resumen")

    def setUsuario(self, usuario):
        self.usuario = usuario
        self.lblUsuario.setText(f"Usuario: {self.usuario}")

    def abrir_boletas(self):
        carpeta_boletas = "Boletas"
        if not os.path.exists(carpeta_boletas):
            os.makedirs(carpeta_boletas)
        QDesktopServices.openUrl(QUrl.fromLocalFile(os.path.abspath(carpeta_boletas)))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ui_VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
