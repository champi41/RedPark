from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog
import sys
import json


class Ui_Resumen(QtWidgets.QDialog):
        
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
        self.btnAtras = QtWidgets.QPushButton(parent=Resumen)
        self.btnAtras.setGeometry(QtCore.QRect(20, 410, 161, 41))
        self.btnAtras.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 20px\n"
"")
        self.btnAtras.setObjectName("btnAtras")
        self.btnAbrirRes = QtWidgets.QPushButton(parent=Resumen)
        self.btnAbrirRes.setGeometry(QtCore.QRect(220, 230, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnAbrirRes.setFont(font)
        self.btnAbrirRes.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-radius: 20px\n"
"")
        self.btnAbrirRes.setObjectName("btnAbrirRes")
        self.btnAbrirRes.clicked.connect(self.abrir_json)
        
        self.retranslateUi(Resumen)
        QtCore.QMetaObject.connectSlotsByName(Resumen)

    def retranslateUi(self, Resumen):
        _translate = QtCore.QCoreApplication.translate
        Resumen.setWindowTitle(_translate("Resumen", "Resumen"))
        self.lblResumen.setText(_translate("Resumen", "Resumen de ventas"))
        self.btnAtras.setText(_translate("Resumen", "Atras"))
        self.btnAbrirRes.setText(_translate("Resumen", "Abrir resumen"))
        
    
    def abrir_json(self):
            
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("JSON files (BaseDato.json)")
        file_dialog.selectNameFilter("JSON files (BaseDato.json)")
        
        if file_dialog.exec():
            file_path = file_dialog.selectedFiles()[0]
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Aquí puedes procesar los datos del archivo JSON como lo necesites
                print(data)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Resumen = Ui_Resumen()
    ui = Ui_Resumen()
    ui.setupResumen(Resumen)
    Resumen.show()
    sys.exit(app.exec())
