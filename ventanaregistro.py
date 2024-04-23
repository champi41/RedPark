from PyQt6 import QtCore, QtGui, QtWidgets
from cliente import cliente

class Ui_registro(QtWidgets.QDialog):
    
    def setupRegistro(self, registro):
        
        
        registro.setObjectName("registro")
        registro.resize(640, 480)
        registro.setStyleSheet("background-color: rgb(0, 0, 90);\n""color: rgb(255, 255, 255);\n""")
        registro.setWindowTitle("Registro RedPark")
        
        self.lblRegistro = QtWidgets.QLabel(parent=registro)
        self.lblRegistro.setGeometry(QtCore.QRect(10, 60, 620, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        self.lblRegistro.setFont(font)
        self.lblRegistro.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblRegistro.setObjectName("lblRegistro")
        
        self.inptNombre = QtWidgets.QLineEdit(parent=registro)
        self.inptNombre.setGeometry(QtCore.QRect(170, 200, 300, 30))
        self.inptNombre.setObjectName("inptNombre")
        self.inptNombre.textChanged.connect(self.almacenar_texto)
        
        
        self.inptPatente = QtWidgets.QLineEdit(parent=registro)
        self.inptPatente.setGeometry(QtCore.QRect(170, 280, 300, 30))
        self.inptPatente.setObjectName("inptPatente")
        self.inptPatente.textChanged.connect(self.almacenar_texto)
        
        self.cliente= None
        
        self.lblNomCon = QtWidgets.QLabel(parent=registro)
        self.lblNomCon.setGeometry(QtCore.QRect(170, 170, 240, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lblNomCon.setFont(font)
        self.lblNomCon.setObjectName("lblNomCon")
        
        self.lblPatente = QtWidgets.QLabel(parent=registro)
        self.lblPatente.setGeometry(QtCore.QRect(170, 250, 240, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lblPatente.setFont(font)
        self.lblPatente.setObjectName("lblPatente")
        
        self.btnIngresar = QtWidgets.QPushButton(parent=registro)
        self.btnIngresar.setGeometry(QtCore.QRect(245, 380, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btnIngresar.setFont(font)
        self.btnIngresar.setStyleSheet("border-radius: 20px;\n""background-color: rgb(255, 0, 4);\n""")
        self.btnIngresar.setObjectName("btnIngresar")
        self.btnIngresar.clicked.connect(self.abrir_ventana_duracion)

        
        self.lblRegistro.setText("Registro")
        self.lblNomCon.setText("Nombre del conductor")
        self.lblPatente.setText("Patente del vehiculo")
        self.btnIngresar.setText("Ingresar")
        
    def almacenar_texto(self):
        
        nombre = self.inptNombre.text()
        patente = self.inptPatente.text()
        self.cliente = cliente(nombre, patente)
   
    def abrir_ventana_duracion(self):
        
        print('Nombre: ', self.cliente.nombre, 'Patente: ', self.cliente.patente)
        
        from ventanaduracion import Ui_duracion
        
        self.ventana_duracion = Ui_duracion()
        self.ventana_duracion.setupDuracion(self.ventana_duracion)
        self.ventana_duracion.show()
       
if __name__ == "__main__":
        
    import sys
    app = QtWidgets.QApplication(sys.argv)
    registro = Ui_registro()
    ui = Ui_registro()
    ui.setupRegistro(registro)
    registro.show()
    sys.exit(app.exec())
