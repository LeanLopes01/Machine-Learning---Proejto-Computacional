import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
import bancoDeDados as bd
import Reconhecimento as re

face = re.ReconhecimentoFacial

class JanelaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Reconhecimento Facial")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        # Campo de entrada de nome
        self.nome_input = QLineEdit(self)
        self.nome_input.setPlaceholderText("Digite seu nome aqui")
        layout.addWidget(self.nome_input)

        # Botão
        self.botao = QPushButton("Exibir Nome no Console", self)
        self.botao.clicked.connect(face.capturar_rosto_autorizado)
        layout.addWidget(self.botao)

        # Rótulo para exibir a confirmação na interface
        self.resultado_label = QLabel("", self)
        layout.addWidget(self.resultado_label)

        # Define o layout
        self.setLayout(layout)

    def mostrar_nome(self):
        nome = self.nome_input.text()  # Obtém o texto do campo de entrada
        print(nome)  # Exibe o nome no console
        self.resultado_label.setText(f"Nome exibido: {nome}")  # Atualiza o rótulo com o nome

# Execução da aplicação
app = QApplication(sys.argv)
janela = JanelaPrincipal()
janela.show()
sys.exit(app.exec())
