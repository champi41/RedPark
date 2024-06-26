from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Lugar(QtWidgets.QDialog):
    
    def setupLugar(self, Lugar):

        Lugar.setObjectName("Lugar")
        Lugar.resize(640, 480)
        Lugar.setStyleSheet("background-color: rgb(0, 0, 90);\n"
"color: rgb(255, 255, 255);")
        self.lblLugar = QtWidgets.QLabel(parent=Lugar)
        self.lblLugar.setGeometry(QtCore.QRect(160, 50, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        self.lblLugar.setFont(font)
        self.lblLugar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblLugar.setObjectName("lblLugar")
        self.btnSiguiente = QtWidgets.QPushButton(parent=Lugar)
        self.btnSiguiente.setGeometry(QtCore.QRect(460, 410, 161, 41))
        self.btnSiguiente.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 20px\n"
"")
        self.btnSiguiente.setObjectName("btnSiguiente")
        self.btnAtras = QtWidgets.QPushButton(parent=Lugar)
        self.btnAtras.setGeometry(QtCore.QRect(20, 410, 161, 41))
        self.btnAtras.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 20px\n"
"")
        self.btnAtras.setObjectName("btnAtras")
        self.A1 = QtWidgets.QCheckBox(parent=Lugar)
        self.A1.setGeometry(QtCore.QRect(120, 150, 76, 20))
        self.A1.setObjectName("A1")
        self.B1 = QtWidgets.QCheckBox(parent=Lugar)
        self.B1.setGeometry(QtCore.QRect(210, 150, 76, 20))
        self.B1.setObjectName("B1")
        self.C1 = QtWidgets.QCheckBox(parent=Lugar)
        self.C1.setGeometry(QtCore.QRect(300, 150, 76, 20))
        self.C1.setObjectName("C1")
        self.D1 = QtWidgets.QCheckBox(parent=Lugar)
        self.D1.setGeometry(QtCore.QRect(390, 150, 76, 20))
        self.D1.setObjectName("D1")
        self.E1 = QtWidgets.QCheckBox(parent=Lugar)
        self.E1.setGeometry(QtCore.QRect(480, 150, 76, 20))
        self.E1.setObjectName("E1")
        self.B2 = QtWidgets.QCheckBox(parent=Lugar)
        self.B2.setGeometry(QtCore.QRect(210, 180, 76, 20))
        self.B2.setObjectName("B2")
        self.C2 = QtWidgets.QCheckBox(parent=Lugar)
        self.C2.setGeometry(QtCore.QRect(300, 180, 76, 20))
        self.C2.setObjectName("C2")
        self.A2 = QtWidgets.QCheckBox(parent=Lugar)
        self.A2.setGeometry(QtCore.QRect(120, 180, 76, 20))
        self.A2.setObjectName("A2")
        self.D2 = QtWidgets.QCheckBox(parent=Lugar)
        self.D2.setGeometry(QtCore.QRect(390, 180, 76, 20))
        self.D2.setObjectName("D2")
        self.E2 = QtWidgets.QCheckBox(parent=Lugar)
        self.E2.setGeometry(QtCore.QRect(480, 180, 76, 20))
        self.E2.setObjectName("E2")
        self.B3 = QtWidgets.QCheckBox(parent=Lugar)
        self.B3.setGeometry(QtCore.QRect(210, 210, 76, 20))
        self.B3.setObjectName("B3")
        self.C3 = QtWidgets.QCheckBox(parent=Lugar)
        self.C3.setGeometry(QtCore.QRect(300, 210, 76, 20))
        self.C3.setObjectName("C3")
        self.A3 = QtWidgets.QCheckBox(parent=Lugar)
        self.A3.setGeometry(QtCore.QRect(120, 210, 76, 20))
        self.A3.setObjectName("A3")
        self.D3 = QtWidgets.QCheckBox(parent=Lugar)
        self.D3.setGeometry(QtCore.QRect(390, 210, 76, 20))
        self.D3.setObjectName("D3")
        self.E3 = QtWidgets.QCheckBox(parent=Lugar)
        self.E3.setGeometry(QtCore.QRect(480, 210, 76, 20))
        self.E3.setObjectName("E3")
        self.B4 = QtWidgets.QCheckBox(parent=Lugar)
        self.B4.setGeometry(QtCore.QRect(210, 240, 76, 20))
        self.B4.setObjectName("B4")
        self.C4 = QtWidgets.QCheckBox(parent=Lugar)
        self.C4.setGeometry(QtCore.QRect(300, 240, 76, 20))
        self.C4.setObjectName("C4")
        self.A4 = QtWidgets.QCheckBox(parent=Lugar)
        self.A4.setGeometry(QtCore.QRect(120, 240, 76, 20))
        self.A4.setObjectName("A4")
        self.D4 = QtWidgets.QCheckBox(parent=Lugar)
        self.D4.setGeometry(QtCore.QRect(390, 240, 76, 20))
        self.D4.setObjectName("D4")
        self.E4 = QtWidgets.QCheckBox(parent=Lugar)
        self.E4.setGeometry(QtCore.QRect(480, 240, 76, 20))
        self.E4.setObjectName("E4")
        self.B5 = QtWidgets.QCheckBox(parent=Lugar)
        self.B5.setGeometry(QtCore.QRect(210, 270, 76, 20))
        self.B5.setObjectName("B5")
        self.C5 = QtWidgets.QCheckBox(parent=Lugar)
        self.C5.setGeometry(QtCore.QRect(300, 270, 76, 20))
        self.C5.setObjectName("C5")
        self.A5 = QtWidgets.QCheckBox(parent=Lugar)
        self.A5.setGeometry(QtCore.QRect(120, 270, 76, 20))
        self.A5.setObjectName("A5")
        self.D5 = QtWidgets.QCheckBox(parent=Lugar)
        self.D5.setGeometry(QtCore.QRect(390, 270, 76, 20))
        self.D5.setObjectName("D5")
        self.E5 = QtWidgets.QCheckBox(parent=Lugar)
        self.E5.setGeometry(QtCore.QRect(480, 270, 76, 20))
        self.E5.setObjectName("E5")
        self.B6 = QtWidgets.QCheckBox(parent=Lugar)
        self.B6.setGeometry(QtCore.QRect(210, 300, 76, 20))
        self.B6.setObjectName("B6")
        self.C6 = QtWidgets.QCheckBox(parent=Lugar)
        self.C6.setGeometry(QtCore.QRect(300, 300, 76, 20))
        self.C6.setObjectName("C6")
        self.A6 = QtWidgets.QCheckBox(parent=Lugar)
        self.A6.setGeometry(QtCore.QRect(120, 300, 76, 20))
        self.A6.setObjectName("A6")
        self.D6 = QtWidgets.QCheckBox(parent=Lugar)
        self.D6.setGeometry(QtCore.QRect(390, 300, 76, 20))
        self.D6.setObjectName("D6")
        self.E6 = QtWidgets.QCheckBox(parent=Lugar)
        self.E6.setGeometry(QtCore.QRect(480, 300, 76, 20))
        self.E6.setObjectName("E6")
        self.B7 = QtWidgets.QCheckBox(parent=Lugar)
        self.B7.setGeometry(QtCore.QRect(210, 330, 76, 20))
        self.B7.setObjectName("B7")
        self.C7 = QtWidgets.QCheckBox(parent=Lugar)
        self.C7.setGeometry(QtCore.QRect(300, 330, 76, 20))
        self.C7.setObjectName("C7")
        self.A7 = QtWidgets.QCheckBox(parent=Lugar)
        self.A7.setGeometry(QtCore.QRect(120, 330, 76, 20))
        self.A7.setObjectName("A7")
        self.D7 = QtWidgets.QCheckBox(parent=Lugar)
        self.D7.setGeometry(QtCore.QRect(390, 330, 76, 20))
        self.D7.setObjectName("D7")
        self.E7 = QtWidgets.QCheckBox(parent=Lugar)
        self.E7.setGeometry(QtCore.QRect(480, 330, 76, 20))
        self.E7.setObjectName("E7")

        Lugar.setWindowTitle("Dialog")
        self.lblLugar.setText("Seleccione su lugar")
        self.btnSiguiente.setText("Siguiente")
        self.btnAtras.setText("Atras")
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


if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Lugar = Ui_Lugar()
    ui = Ui_Lugar()
    ui.setupLugar(Lugar)
    Lugar.show()
    sys.exit(app.exec())
