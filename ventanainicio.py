from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_VentanaPrincipal(object):
    
    def setupUi(self, VentanaPrincipal):
        
        VentanaPrincipal.setObjectName("VentanaPrincipal")
        VentanaPrincipal.resize(640, 480)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(22)
        VentanaPrincipal.setFont(font)
        VentanaPrincipal.setStyleSheet("background-color: rgb(0, 0, 90);\n""color: rgb(255, 255, 255);\n""")
        
        self.centralwidget = QtWidgets.QWidget(parent=VentanaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        
        #titulo redpark
        self.lblRedBank = QtWidgets.QLabel(parent=self.centralwidget)
        #medidas y posision
        self.lblRedBank.setGeometry(QtCore.QRect(135, 80, 370, 120))
        #fuente y tipo de fuente
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(50)
        self.lblRedBank.setFont(font)
        #aliniacion de texto
        self.lblRedBank.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblRedBank.setObjectName("lblRedBank")
        self.lblRedBank.setText("<html><head/><body><p><span style=\" font-size:72pt; font-style:italic; color:#ffffff;\">Red</span><span style=\" font-size:72pt; font-weight:700; color:#ff0004;\">Park</span></p></body></html>")
        
        self.btnTicket = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnTicket.setGeometry(QtCore.QRect(225, 240, 190, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnTicket.setFont(font)
        self.btnTicket.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btnTicket.setStyleSheet("background-color: rgb(255, 0, 4);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.btnTicket.setObjectName("btnTicket")
        self.btnTicket.clicked.connect(self.abrir_ventana_registro)
        self.btnTicket.setText("Obtener Ticket")
        
        VentanaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=VentanaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setStyleSheet("border: solid black;")
        self.menubar.setObjectName("menubar")
        self.menuMas = QtWidgets.QMenu(parent=self.menubar)
        self.menuMas.setObjectName("menuMas")
        self.menuMas.setTitle("Mas")
        VentanaPrincipal.setMenuBar(self.menubar)
        self.actionTotal_de_Tickets = QtGui.QAction(parent=VentanaPrincipal)
        self.actionTotal_de_Tickets.setObjectName("actionTotal_de_Tickets")
        self.actionTotal_de_Tickets.setText("Total de Tickets")
        self.menuMas.addAction(self.actionTotal_de_Tickets)
        self.menubar.addAction(self.menuMas.menuAction())
  
    def abrir_ventana_registro(self):
        
        from ventanaregistro import Ui_registro
        
        self.ventana_registro = Ui_registro()
        self.ventana_registro.setupRegistro(self.ventana_registro)
        self.ventana_registro.show()

if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_VentanaPrincipal()
    ui.setupUi(VentanaPrincipal)
    VentanaPrincipal.show()
    sys.exit(app.exec())
