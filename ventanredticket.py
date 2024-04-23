from PyQt6 import QtCore, QtGui, QtWidgets
from ventanaduracion import boton

class Ui_RedTicket(QtWidgets.QDialog):
    
    def setupRedTicket(self, RedTicket):
        
        RedTicket.setObjectName("RedTicket")
        RedTicket.resize(640, 480)
        RedTicket.setStyleSheet("background-color: rgb(0, 0, 90);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.lblRedTicket = QtWidgets.QLabel(parent=RedTicket)
        self.lblRedTicket.setGeometry(QtCore.QRect(10, 60, 620, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        self.lblRedTicket.setFont(font)
        self.lblRedTicket.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblRedTicket.setObjectName("lblRedTicket")
        
        self.lblDuracionTicket = QtWidgets.QLabel(parent=RedTicket)
        self.lblDuracionTicket.setGeometry(QtCore.QRect(160, 170, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lblDuracionTicket.setFont(font)
        self.lblDuracionTicket.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblDuracionTicket.setObjectName("lblDuracionTicket")
        
        self.lblNombreTicket = QtWidgets.QLabel(parent=RedTicket)
        self.lblNombreTicket.setGeometry(QtCore.QRect(160, 230, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lblNombreTicket.setFont(font)
        self.lblNombreTicket.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblNombreTicket.setObjectName("lblNombreTicket")
        
        self.lblPatenteTicket = QtWidgets.QLabel(parent=RedTicket)
        self.lblPatenteTicket.setGeometry(QtCore.QRect(160, 290, 90, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lblPatenteTicket.setFont(font)
        self.lblPatenteTicket.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblPatenteTicket.setObjectName("lblPatenteTicket")
        
        self.lblDuracionDatos = QtWidgets.QLabel(parent=RedTicket)
        self.lblDuracionDatos.setGeometry(QtCore.QRect(260, 170, 251, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lblDuracionDatos.setFont(font)
        self.lblDuracionDatos.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblDuracionDatos.setObjectName("lblDuracionDatos")
        
        self.lblNombreDatos = QtWidgets.QLabel(parent=RedTicket)
        self.lblNombreDatos.setGeometry(QtCore.QRect(260, 230, 251, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lblNombreDatos.setFont(font)
        self.lblNombreDatos.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblNombreDatos.setObjectName("lblNombreDatos")
        
        self.lblPatenteDatos = QtWidgets.QLabel(parent=RedTicket)
        self.lblPatenteDatos.setGeometry(QtCore.QRect(260, 290, 251, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lblPatenteDatos.setFont(font)
        self.lblPatenteDatos.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lblPatenteDatos.setObjectName("lblPatenteDatos")
        
        self.lblAviso2 = QtWidgets.QLabel(parent=RedTicket)
        self.lblAviso2.setGeometry(QtCore.QRect(130, 390, 411, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lblAviso2.setFont(font)
        self.lblAviso2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblAviso2.setObjectName("lblAviso2")

        RedTicket.setWindowTitle("RedTicket")
        self.lblRedTicket.setText("<html><head/><body><p>Red<span style=\" color:#ff0004;\">Ticket</span></p></body></html>")
        self.lblDuracionTicket.setText("Duración:")
        self.lblNombreTicket.setText("Nombre:")
        self.lblPatenteTicket.setText("Patente:")
        self.lblAviso2.setText("Puede cerrar las ventanas")

        xd = boton
        print('esto vale xd: ', xd)
        if boton == 15:
            self.lblDuracionDatos.setText("15 minutos")
            self.lblNombreDatos.setText("")
            self.lblPatenteDatos.setText("")
        
        elif boton == 30:
            
            self.lblDuracionDatos.setText("30 minutos")
            self.lblNombreDatos.setText("")
            self.lblPatenteDatos.setText("")
            
        elif boton == 1:
            
            self.lblDuracionDatos.setText("1 hora")
            self.lblNombreDatos.setText("")
            self.lblPatenteDatos.setText("")
            
        elif boton == 2:
            
            self.lblDuracionDatos.setText("2 horas")
            self.lblNombreDatos.setText("")
            self.lblPatenteDatos.setText("")
        
        elif boton == 3:
            
            self.lblDuracionDatos.setText("3 horas")
            self.lblNombreDatos.setText("")
            self.lblPatenteDatos.setText("")
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RedTicket = Ui_RedTicket()
    ui = Ui_RedTicket()
    ui.setupRedTicket(RedTicket)
    RedTicket.show()
    sys.exit(app.exec())
