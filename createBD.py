'''
Este código cria o banco de dados .bd com as colunas: id (chave primária), nome, data_hora e valores_landmarks.
'''

import sqlite3

conexao = sqlite3.connect("reconhecimento_facial.db")
cursor = conexao.cursor()

#tabela de reconhecimento facial
cursor.execute('''
CREATE TABLE IF NOT EXISTS reconhecimento_facial (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    data_hora TEXT NOT NULL,
    valores_landmarks TEXT
)
''')
conexao.commit()
