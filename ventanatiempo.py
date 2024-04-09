from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_VentanaTiempo(object):
    def setupTiempo(self, VentanaTiempo):
        VentanaTiempo.setObjectName("VentanaTiempo")
        VentanaTiempo.resize(640, 480)
        VentanaTiempo.setStyleSheet("background-color: rgb(0, 0, 90);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=VentanaTiempo)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 621, 101))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.min15btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.min15btn.setGeometry(QtCore.QRect(60, 183, 81, 133))
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
        self.min30btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.min30btn.setGeometry(QtCore.QRect(170, 183, 81, 133))
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
        self.hora1btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.hora1btn.setGeometry(QtCore.QRect(280, 183, 81, 133))
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
        self.hora2btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.hora2btn.setGeometry(QtCore.QRect(390, 183, 81, 133))
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
        self.hora3btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.hora3btn.setGeometry(QtCore.QRect(500, 183, 81, 133))
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
        VentanaTiempo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=VentanaTiempo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        VentanaTiempo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=VentanaTiempo)
        self.statusbar.setObjectName("statusbar")
        VentanaTiempo.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaTiempo)
        QtCore.QMetaObject.connectSlotsByName(VentanaTiempo)

    def retranslateUi(self, VentanaTiempo):
        _translate = QtCore.QCoreApplication.translate
        VentanaTiempo.setWindowTitle(_translate("VentanaTiempo", "Duracion"))
        self.label.setText(_translate("VentanaTiempo", "Seleccione el tiempo "))
        self.min15btn.setText(_translate("VentanaTiempo", "15\n"
"Minutos"))
        self.min30btn.setText(_translate("VentanaTiempo", "30\n"
"Minutos"))
        self.hora1btn.setText(_translate("VentanaTiempo", "1\n"
"Hora"))
        self.hora2btn.setText(_translate("VentanaTiempo", "2\n"
"Horas"))
        self.hora3btn.setText(_translate("VentanaTiempo", "3\n"
"Horas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaTiempo = QtWidgets.QMainWindow()
    ui = Ui_VentanaTiempo()
    ui.setupTiempo(VentanaTiempo)
    VentanaTiempo.show()
    sys.exit(app.exec())
