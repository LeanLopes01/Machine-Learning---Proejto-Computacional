import sqlite3
import pandas as pd
from datetime import datetime

#conecta ao banco de dados sqlite3
conexao = sqlite3.connect("reconhecimento_facial.db")
cursor = conexao.cursor()

class RegistroBD:

    def __init__(self, nome, dadosRegistro):
        self.DR = dadosRegistro
        self.nome = nome

    def verifica_registro(self):
        cursor.execute('SELECT COUNT(*) nome FROM reconhecimento_facial WHERE nome = ?', (self.nome,))
        resultado = cursor.fetchone()
        return resultado[0]>0

    #funcao pra registrar dados de reconhecimento facial
    def registrar_reconhecimento(self):

        if self.verifica_registro():
            print(f"Já existe um registro com o nome {self.nome}. Registro não realizado.")
            return
        
        data_hora = datetime.now().isoformat()

        df_landmarks = pd.DataFrame(self.DR, columns=['x', 'y', 'z']) #transforma landmarcks em dataframes do pandas
        valores_landmarks = df_landmarks.values.flatten().tolist() #lista de valores dos landmarks
    
        # Inserir os dados no banco de dados
        cursor.execute('''
            INSERT INTO reconhecimento_facial (
                nome, data_hora, 
                landmark_0_x, landmark_0_y, landmark_0_z,
                landmark_1_x, landmark_1_y, landmark_1_z,
                landmark_2_x, landmark_2_y, landmark_2_z,
                landmark_3_x, landmark_3_y, landmark_3_z,
                landmark_4_x, landmark_4_y, landmark_4_z,
                landmark_5_x, landmark_5_y, landmark_5_z,
                landmark_6_x, landmark_6_y, landmark_6_z,
                landmark_7_x, landmark_7_y, landmark_7_z,
                landmark_8_x, landmark_8_y, landmark_8_z,
                landmark_9_x, landmark_9_y, landmark_9_z,
                landmark_10_x, landmark_10_y, landmark_10_z,
                landmark_11_x, landmark_11_y, landmark_11_z,
                landmark_12_x, landmark_12_y, landmark_12_z
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', [self.nome, data_hora] + valores_landmarks)
    
        conexao.commit()
        print(f"Dados de reconhecimento facial para {self.nome} registrados com sucesso.")

if __name__ == '__main__':

    #exemplos de landmarcks
    landmarks_exemplo = [
        {"x": 0.5, "y": 0.5, "z": 0.1},
        {"x": 0.6, "y": 0.6, "z": 0.2},
        {"x": 0.7, "y": 0.7, "z": 0.3},
        {"x": 0.8, "y": 0.8, "z": 0.4},
        {"x": 0.9, "y": 0.9, "z": 0.5},
        {"x": 1.0, "y": 1.0, "z": 0.6},
        {"x": 1.1, "y": 1.1, "z": 0.7},
        {"x": 1.2, "y": 1.2, "z": 0.8},
        {"x": 1.3, "y": 1.3, "z": 0.9},
        {"x": 1.4, "y": 1.4, "z": 1.0},
        {"x": 1.5, "y": 1.5, "z": 1.1},
        {"x": 1.6, "y": 1.6, "z": 1.2},
        {"x": 1.7, "y": 1.7, "z": 1.3},
    ]

    #registrar usuário
    r=RegistroBD("Lean Lopes", landmarks_exemplo)
    r.registrar_reconhecimento()

conexao.close()
