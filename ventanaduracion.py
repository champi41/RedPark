from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_duracion(QtWidgets.QDialog):
        
    def setupDuracion(self, tiempo):
            
        tiempo.setObjectName("tiempo")
        tiempo.resize(640, 480)
        tiempo.setStyleSheet("background-color: rgb(0, 0, 90);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.hora1btn = QtWidgets.QPushButton(parent=tiempo)
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
        
        self.min30btn = QtWidgets.QPushButton(parent=tiempo)
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
        
        self.hora3btn = QtWidgets.QPushButton(parent=tiempo)
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
        
        self.label = QtWidgets.QLabel(parent=tiempo)
        self.label.setGeometry(QtCore.QRect(10, 60, 620, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        
        self.hora2btn = QtWidgets.QPushButton(parent=tiempo)
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
        
        self.min15btn = QtWidgets.QPushButton(parent=tiempo)
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
        
        self.lbl600 = QtWidgets.QLabel(parent=tiempo)
        self.lbl600.setGeometry(QtCore.QRect(60, 310, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl600.setFont(font)
        self.lbl600.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl600.setObjectName("lbl600")
        
        self.lbl1050 = QtWidgets.QLabel(parent=tiempo)
        self.lbl1050.setGeometry(QtCore.QRect(170, 310, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl1050.setFont(font)
        self.lbl1050.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl1050.setObjectName("lbl1050")
        
        self.lbl1800 = QtWidgets.QLabel(parent=tiempo)
        self.lbl1800.setGeometry(QtCore.QRect(280, 310, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl1800.setFont(font)
        self.lbl1800.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl1800.setObjectName("lbl1800")
        
        self.lbl3000 = QtWidgets.QLabel(parent=tiempo)
        self.lbl3000.setGeometry(QtCore.QRect(390, 310, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl3000.setFont(font)
        self.lbl3000.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl3000.setObjectName("lbl3000")
        
        self.lbl3600 = QtWidgets.QLabel(parent=tiempo)
        self.lbl3600.setGeometry(QtCore.QRect(500, 310, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lbl3600.setFont(font)
        self.lbl3600.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl3600.setObjectName("lbl3600")
        
        self.lblAviso = QtWidgets.QLabel(parent=tiempo)
        self.lblAviso.setGeometry(QtCore.QRect(58, 360, 521, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.lblAviso.setFont(font)
        self.lblAviso.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblAviso.setObjectName("lblAviso")

        tiempo.setWindowTitle("Duracion")
        self.hora1btn.setText("1\n""Hora")
        self.min30btn.setText("30\n""Minutos")
        self.hora3btn.setText("3\n""Horas")
        self.label.setText("Seleccione el tiempo")
        self.hora2btn.setText("2\n""Horas")
        self.min15btn.setText("15\n""Minutos")
        self.lbl600.setText("$600")
        self.lbl1050.setText("$1050")
        self.lbl1800.setText("$1800")
        self.lbl3000.setText("$3000")
        self.lbl3600.setText("$3600")
        self.lblAviso.setText("Si excede el tiempo que ingresó, se le cobrará $45 por cada minuto excedido.")
        
          
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tiempo = Ui_duracion()
    ui = Ui_duracion()
    ui.setupDuracion(tiempo)
    tiempo.show()
    sys.exit(app.exec())
