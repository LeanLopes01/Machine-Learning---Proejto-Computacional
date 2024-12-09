'''
Este é o grosso do código mesmo, é aqui onde temos a interface do nosso reconhimento facial e onde podemos registrar novos usuários e detectar suspeitos.
É onde também o código reconhece se há um usuário registrado, e se não houver ele reconhece a pessoa como "suspeito detectado"
E sim, o botão SAIR funciona.
'''

import reconhecimento_facial as rf
import bancoDeDados as bd
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog, QLineEdit, QDialogButtonBox, QLabel
)

class Janela_Principal(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(454, 677)
        self.buttonSair = QtWidgets.QPushButton(parent=Form)
        self.buttonSair.setGeometry(QtCore.QRect(190, 200, 61, 51))
        self.buttonSair.setStyleSheet("QPushButton{\n"
"    \n"
"    font: 10pt \"Sans Serif Collection\";\n"
"    border-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(235, 133, 122, 255));\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(227, 49, 26, 255));\n"
"    border-radius: 25px;\n"
"}")
        self.buttonSair.setObjectName("buttonSair")
        self.buttonDetectarPessoas = QtWidgets.QPushButton(parent=Form)
        self.buttonDetectarPessoas.setGeometry(QtCore.QRect(110, 130, 221, 61))
        self.buttonDetectarPessoas.setStyleSheet("QPushButton{\n"
"    \n"
"    font: 20pt \"Sans Serif Collection\";\n"
"    border-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(235, 133, 122, 255));\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(227, 49, 26, 255));\n"
"    border-radius: 25px;\n"
"}")
        self.buttonDetectarPessoas.setObjectName("buttonDetectarPessoas")
        self.buttonRegistrarRosto = QtWidgets.QPushButton(parent=Form)
        self.buttonRegistrarRosto.setGeometry(QtCore.QRect(110, 60, 221, 61))
        self.buttonRegistrarRosto.setStyleSheet("QPushButton{\n"
"    \n"
"    font: 20pt \"Sans Serif Collection\";\n"
"    border-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(235, 133, 122, 255));\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0, stop:1 rgba(227, 49, 26, 255));\n"
"    border-radius: 25px;\n"
"}")
        self.buttonRegistrarRosto.setObjectName("buttonRegistrarRosto")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 691, 51))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(-10, 0, 471, 681))
        self.label_2.setStyleSheet("background-color: rgb(99, 82, 222);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(90, 270, 251, 381))
        self.label_6.setStyleSheet("background-color: rgb(0, 168, 168);\n"
"border-radius:25px")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=Form)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 300, 181, 321))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2.raise_()
        self.buttonSair.raise_()
        self.buttonDetectarPessoas.raise_()
        self.buttonRegistrarRosto.raise_()
        self.label.raise_()
        self.label_6.raise_()
        self.textEdit_2.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.buttonRegistrarRosto.clicked.connect(self.Registrar_Rosto)
        self.buttonDetectarPessoas.clicked.connect(self.Detectar_Pessoa)
        self.buttonSair.clicked.connect(self.sair)
        self.lista_nomes_registrados()

    def lista_nomes_registrados(self):
        sb = bd.SelecaoTodosNomes()
        pessoas_autorizadas = sb.SelecionarTodosNomes()
        nomes_autorizados = []
        for pessoa in pessoas_autorizadas:
                nomes_autorizados.append(pessoa["nome"])
        nomes_como_string = ", ".join(nomes_autorizados)
        self.textEdit_2.setText(nomes_como_string)

    def Registrar_Rosto(self):
        try:
          dialog = PopUpDialog()
          if dialog.exec():
              nome = dialog.get_name()
              print(f"Nome inserido: {nome}")
        except:
            print("Erro ao registrar rosto")
        
        self.nome = nome

        r = rf.Reconhecimento(self.nome)
        r.capturar_rosto_autorizado()
        self.lista_nomes_registrados()

    def Detectar_Pessoa(self):
        bd.SelecaoTodosNomes()
        self.nome = bd.SelecaoTodosNomes()
        r = rf.Reconhecimento(self.nome)
        r.detectar_suspeitos()    

    def sair(self):
        sys.exit(app.exec())
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.buttonSair.setText(_translate("Form", "Sair"))
        self.buttonDetectarPessoas.setText(_translate("Form", "Detectar Pessoa"))
        self.buttonRegistrarRosto.setText(_translate("Form", "Registrar Rosto"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Escolha uma das opções abaixo:</span></p></body></html>"))

class PopUpDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inserir Nome")

        self.layout = QVBoxLayout()
        self.label = QLabel("Digite seu nome:")
        self.line_edit = QLineEdit()
        self.buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.buttons)
        self.setLayout(self.layout)

        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

    def get_name(self):
        return self.line_edit.text()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Janela_Principal()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
