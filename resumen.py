class Ui_Resumen(QtWidgets.QWidget):
     
    def __init__(self, parent):
        
        super().__init__(parent)
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
        self.lblUsuario.setGeometry(QtCore.QRect(20, 150, 75, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lblUsuario.setFont(font)
        self.lblUsuario.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblUsuario.setObjectName("lblUsuario")
        self.lblUsuario.setText("Usuario: ")
        
        self.lblNombreUsu = QtWidgets.QLabel(parent=self)
        self.lblNombreUsu.setGeometry(QtCore.QRect(100, 150, 75, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lblNombreUsu.setFont(font)
        self.lblNombreUsu.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblNombreUsu.setObjectName("lblNombreUsu")
        self.lblNombreUsu.setText("Nombre")
        
        self.btnAtras = QtWidgets.QPushButton(parent=self)
        self.btnAtras.setGeometry(QtCore.QRect(20, 410, 161, 41))
        self.btnAtras.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 20px\n"
"")
        self.btnAtras.setObjectName("btnAtras")
        self.btnAbrirRes = QtWidgets.QPushButton(parent=self)
        self.btnAbrirRes.setGeometry(QtCore.QRect(220, 230, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnAbrirRes.setFont(font)
        self.btnAbrirRes.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 20px\n"
"")
        self.btnAbrirRes.setObjectName("btnAbrirRes")

        self.setWindowTitle("Resumen")
        self.lblResumen.setText("Resumen de ventas")
        self.btnAtras.setText("Atras")
        self.btnAbrirRes.setText("Abrir resumen")
