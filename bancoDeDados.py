import sqlite3
import json
from datetime import datetime

class SelecaoTodosNomes:

    def __init__(self):
        self.nomo = None
        self.connection = None
        self.cursor = None
        self.open_connection()

    def open_connection(self):
        if not self.connection:
            self.connection = sqlite3.connect("reconhecimento_facial.db")
            self.cursor = self.connection.cursor()

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None

    def SelecionarTodosNomes(self):
        if self.connection is None:
            self.open_connection()

        self.cursor.execute('SELECT nome, valores_landmarks FROM reconhecimento_facial')
        resultados = self.cursor.fetchall()

        pessoas = []
        for resultado in resultados:
            nome = resultado[0]
            # Deserializar os landmarks (assumindo que estão armazenados como JSON)
            valores_landmarks = json.loads(resultado[1])
            pessoas.append({"nome": nome, "face_encoding": valores_landmarks})

        return pessoas


class SelecaoDadosBD:

    def __init__(self, dado):
        self.dado = dado
        self.connection = None
        self.cursor = None
        self.open_connection()

    def open_connection(self):
        if not self.connection:
            self.connection = sqlite3.connect("reconhecimento_facial.db")
            self.cursor = self.connection.cursor()

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None

    def seleciona_nome(self):
        if self.connection is None:
            self.open_connection()

        self.cursor.execute('SELECT nome FROM reconhecimento_facial WHERE nome = ?', (self.dado,))
        name = self.cursor.fetchone()
        if name:
            return name[0]
        else:
            print(f"No record found for {self.nome}.")
            return None
        
    def selecionar_rosto_bd(self):
        if self.connection is None:
            self.open_connection()

        self.cursor.execute('''
        SELECT valores_landmarks FROM reconhecimento_facial WHERE nome = ?''', (self.dado,))
        resultado = self.cursor.fetchone()
        return resultado    

    def __del__(self):
        self.close_connection()

class RegistroBD:

    def __init__(self, nome, dadosRegistro):
        self.DR = dadosRegistro
        self.nome = nome
        self.connection = None
        self.cursor = None
        self.open_connection()

    def open_connection(self):
        if not self.connection:
            self.connection = sqlite3.connect("reconhecimento_facial.db")
            self.cursor = self.connection.cursor()

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None
    
    def verifica_registro(self):
        if self.connection is None:
            self.open_connection()

        self.cursor.execute('SELECT COUNT(*) FROM reconhecimento_facial WHERE nome = ?', (self.nome,))
        resultado = self.cursor.fetchone()
        return resultado[0]>0

    #funcao pra registrar dados de reconhecimento facial
    def registrar_reconhecimento(self):

        if self.verifica_registro():
            print(f"Já existe um registro com o nome {self.nome}. Registro não realizado.")
            return
        
        data_hora = datetime.now().isoformat()

        #df_landmarks = pd.DataFrame(self.DR, columns=['x', 'y', 'z']) #transforma landmarcks em dataframes do pandas
        #valores_landmarks = df_landmarks.values.flatten().tolist() #lista de valores dos landmarks
        valores_json = json.dumps(self.DR)

        # Inserir os dados no banco de dados
        self.cursor.execute('''
            INSERT INTO reconhecimento_facial (nome, data_hora, valores_landmarks) VALUES (?, ?, ?)''', (self.nome, data_hora, valores_json))
    
        self.connection.commit()
        print(f"Dados de reconhecimento facial para {self.nome} registrados com sucesso.")

    def __del__(self):
        self.close_connection()

if __name__ == '__main__':
    landmarks_exemplo = [
        {"x": 0.5, "y": 0.5, "z": 0.1}, {"x": 0.6, "y": 0.6, "z": 0.2}
    ]

    r = RegistroBD("Lean Lopes", landmarks_exemplo)
    r.registrar_reconhecimento()