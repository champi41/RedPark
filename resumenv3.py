from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl
import json
import os

class Ui_Resumen(QtWidgets.QDialog):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario

    def setupResumen(self, Resumen):
        Resumen.setObjectName("Resumen")
        Resumen.resize(640, 480)
        Resumen.setStyleSheet("background-color: rgb(0, 0, 90);\n"
                              "color: rgb(255, 255, 255);")
        self.lblResumen = QtWidgets.QLabel(parent=Resumen)
        self.lblResumen.setGeometry(QtCore.QRect(160, 50, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(28)
        self.lblResumen.setFont(font)
        self.lblResumen.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblResumen.setObjectName("lblResumen")

        self.lblUsuario = QtWidgets.QLabel(parent=Resumen)
        self.lblUsuario.setGeometry(QtCore.QRect(160, 100, 320, 50))
        font.setPointSize(14)
        self.lblUsuario.setFont(font)
        self.lblUsuario.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblUsuario.setObjectName("lblUsuario")

        self.btnAtras = QtWidgets.QPushButton(parent=Resumen)
        self.btnAtras.setGeometry(QtCore.QRect(20, 410, 161, 41))
        self.btnAtras.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                    "border-radius: 20px\n"
                                    "")
        self.btnAtras.setObjectName("btnAtras")
        self.btnAbrirRes = QtWidgets.QPushButton(parent=Resumen)
        self.btnAbrirRes.setGeometry(QtCore.QRect(220, 230, 201, 51))
        font.setPointSize(14)
        self.btnAbrirRes.setFont(font)
        self.btnAbrirRes.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                       "border-radius: 20px\n"
                                       "")
        self.btnAbrirRes.setObjectName("btnAbrirRes")
        self.btnAbrirRes.clicked.connect(self.abrir_boletas)

        self.retranslateUi(Resumen)
        QtCore.QMetaObject.connectSlotsByName(Resumen)

    def retranslateUi(self, Resumen):
        _translate = QtCore.QCoreApplication.translate
        Resumen.setWindowTitle(_translate("Resumen", "Resumen"))
        self.lblResumen.setText(_translate("Resumen", "Resumen de ventas"))
        self.lblUsuario.setText(_translate("Resumen", f"Usuario: {self.usuario}"))
        self.btnAtras.setText(_translate("Resumen", "Atrás"))
        self.btnAbrirRes.setText(_translate("Resumen", "Abrir resumen"))

    def abrir_boletas(self):
        carpeta_boletas = "Boletas"
        if not os.path.exists(carpeta_boletas):
            os.makedirs(carpeta_boletas)
        QDesktopServices.openUrl(QUrl.fromLocalFile(os.path.abspath(carpeta_boletas)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    usuario = "nombre_del_usuario"  # Este debería ser el nombre del usuario que ha iniciado sesión
    Resumen = Ui_Resumen(usuario)
    ui = Ui_Resumen(usuario)
    ui.setupResumen(Resumen)
    Resumen.show()
    sys.exit(app.exec())