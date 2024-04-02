from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        VentanaPrincipal.setObjectName("VentanaPrincipal")
        VentanaPrincipal.resize(640, 480)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(22)
        VentanaPrincipal.setFont(font)
        VentanaPrincipal.setStyleSheet("background-color: rgb(0, 0, 90);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=VentanaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.lblRedBank = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblRedBank.setGeometry(QtCore.QRect(135, 80, 370, 120))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(50)
        self.lblRedBank.setFont(font)
        self.lblRedBank.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblRedBank.setObjectName("lblRedBank")
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
        VentanaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=VentanaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setStyleSheet("border: solid black;")
        self.menubar.setObjectName("menubar")
        self.menuMas = QtWidgets.QMenu(parent=self.menubar)
        self.menuMas.setObjectName("menuMas")
        VentanaPrincipal.setMenuBar(self.menubar)
        self.actionTotal_de_Tickets = QtGui.QAction(parent=VentanaPrincipal)
        self.actionTotal_de_Tickets.setObjectName("actionTotal_de_Tickets")
        self.menuMas.addAction(self.actionTotal_de_Tickets)
        self.menubar.addAction(self.menuMas.menuAction())

        self.retranslateUi(VentanaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(VentanaPrincipal)

    def retranslateUi(self, VentanaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        VentanaPrincipal.setWindowTitle(_translate("VentanaPrincipal", "Inicio RedBank"))
        self.lblRedBank.setText(_translate("VentanaPrincipal", "<html><head/><body><p><span style=\" font-size:72pt; font-style:italic; color:#ffffff;\">Red</span><span style=\" font-size:72pt; font-weight:700; color:#ff0004;\">Park</span></p></body></html>"))
        self.btnTicket.setText(_translate("VentanaPrincipal", "Obtener Ticket"))
        self.menuMas.setTitle(_translate("VentanaPrincipal", "Mas"))
        self.actionTotal_de_Tickets.setText(_translate("VentanaPrincipal", "Total de Tickets"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_VentanaPrincipal()
    ui.setupUi(VentanaPrincipal)
    VentanaPrincipal.show()
    sys.exit(app.exec())
