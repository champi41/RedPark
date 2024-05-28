from PyQt6 import QtCore, QtGui, QtWidgets
from cliente import cliente
from ticket import ticket
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
        self.setStyleSheet("background-color: rgb(0, 0, 90);\n""color: rgb(255, 255, 255);\n""")
        
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
        self.btnTicket.setText("Obtener Ticket")
        self.btnTicket.clicked.connect(self.showRegistro)
        
        self.menubar = QtWidgets.QMenuBar(parent=self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setStyleSheet("border: solid black;")
        self.menubar.setObjectName("menubar")
        self.menuMas = QtWidgets.QMenu(parent=self.menubar)
        self.menuMas.setObjectName("menuMas")
        self.menuMas.setTitle("Mas")
        self.setMenuBar(self.menubar)
        self.actionTotal_de_Tickets = QtGui.QAction(parent=self)
        self.actionTotal_de_Tickets.setObjectName("actionTotal_de_Tickets")
        self.actionTotal_de_Tickets.setText("Total de Tickets")
        self.menuMas.addAction(self.actionTotal_de_Tickets)
        self.menubar.addAction(self.menuMas.menuAction())
        
        self.registro = Registro(self)
        self.registro.hide()
        
        self.duracion = Duracion(self)
        self.duracion.hide()
        
        self.redticket = RedTicket(self)
        self.redticket.hide()
        

        
    def showRegistro(self):
        
        self.redPark.hide()
        self.registro.show()
        self.registro.limpiar()
        
    def showDuracion(self):
        
        self.registro.hide()
        self.duracion.show()
        
    def showRedTicket(self,boton, nombre="", patente=""):
        
        self.duracion.hide()
        nombre = self.registro.inptNombre.text()
        patente = self.registro.inptPatente.text()
        self.redticket.setupRedTicket(nombre, patente, boton)
        self.redticket.show()
        self.registro.almacenar_cliente()
    def retornar(self):
        
        self.redticket.hide()
        self.redPark.show()
        
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
        
        self.inptPatente = QtWidgets.QLineEdit(parent=self)
        self.inptPatente.setGeometry(QtCore.QRect(170, 280, 300, 30))
        self.inptPatente.setObjectName("inptPatente")
        
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
        self.btnIngresar.setGeometry(QtCore.QRect(245, 380, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btnIngresar.setFont(font)
        self.btnIngresar.setStyleSheet("border-radius: 20px;\n""background-color: rgb(255, 0, 4);\n""")
        self.btnIngresar.setObjectName("btnIngresar")
        self.btnIngresar.clicked.connect(self.parent().showDuracion)

        self.lblRegistro.setText("Registro")
        self.lblNomCon.setText("Nombre del conductor")
        self.lblPatente.setText("Patente del vehiculo")
        self.btnIngresar.setText("Ingresar")
    
    def limpiar(self):
        
        self.inptNombre.clear()
        self.inptPatente.clear()    
        
    def almacenar_cliente(self):
        
        nombre = self.inptNombre.text()
        patente = self.inptPatente.text()
        self.cliente = cliente(nombre, patente)
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
        self.min15btn.clicked.connect(lambda: self.parent().showRedTicket(0,25))
        
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
        
        self.lbl600.setText("$600")
        self.lbl1050.setText("$1050")
        self.lbl1800.setText("$1800")
        self.lbl3000.setText("$3000")
        self.lbl3600.setText("$3600")
        self.lblAviso.setText("Si excede el tiempo que ingresó, se le cobrará $45 por cada minuto excedido.")
        
        


class RedTicket(QtWidgets.QWidget):
    
    def __init__(self, parent):
        
        super().__init__(parent)
        self.setupRedTicket( nombre="", patente="",)
    def almacenar_ticket(self, boton):
        nombre = self.parent().registro.inptNombre.text()
        patente = self.parent().registro.inptPatente.text()
        duracion = str(boton)
        precio = boton * 1000
        self.ticket = ticket(nombre, patente, duracion)
    def Crear_Boleta(self, boton):
        self.almacenar_ticket(boton)
        timestamp = datetime.now().strftime("%H, %M, %S, %d, %m, %Y")
        file_name = f"ticket_{timestamp}.json"
        ticket_aux = {
            "Nombre":  self.parent().registro.inptNombre.text(),
            "Patente":  self.parent().registro.inptPatente.text(),
            "Duracion": str(boton) + "hrs",
            "Precio": boton * 1000
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
        
        self.lblDuracion = QtWidgets.QLabel(parent=self)
        self.lblDuracion.setGeometry(QtCore.QRect(90, 280, 240, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lblDuracion.setFont(font)
        self.lblDuracion.setObjectName("lblDuracion")
        
        self.btnGuardarTicket = QtWidgets.QPushButton(parent=self)
        self.btnGuardarTicket.setGeometry(QtCore.QRect(250, 370, 150, 40))
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
        self.lblTicket.setText("Ticket RedPark")
        self.lblNombre.setText("Nombre del conductor: " + self.parent().registro.inptNombre.text())
        self.lblPatente.setText("Patente del vehiculo: " + self.parent().registro.inptPatente.text())
        self.lblDuracion.setText("Duracion del Ticket: " + str(boton) + " horas")
        
        precio_total = boton * 1800
        
        self.lblPrecio = QtWidgets.QLabel(parent=self)
        self.lblPrecio.setGeometry(QtCore.QRect(90, 320, 240, 21))
        font.setPointSize(14)
        self.lblPrecio.setFont(font)
        self.lblPrecio.setObjectName("lblPrecio")
        self.lblPrecio.setText("Precio: $" + str(precio_total))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = Ui_VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
