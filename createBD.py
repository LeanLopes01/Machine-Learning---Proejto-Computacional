import sqlite3

conexao = sqlite3.connect("reconhecimento_facial.db")
cursor = conexao.cursor()

#tabela de reconhecimento facial
cursor.execute('''
CREATE TABLE IF NOT EXISTS reconhecimento_facial (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    data_hora TEXT NOT NULL,
    landmark_0_x REAL, landmark_0_y REAL, landmark_0_z REAL,
    landmark_1_x REAL, landmark_1_y REAL, landmark_1_z REAL,
    landmark_2_x REAL, landmark_2_y REAL, landmark_2_z REAL,
    landmark_3_x REAL, landmark_3_y REAL, landmark_3_z REAL,
    landmark_4_x REAL, landmark_4_y REAL, landmark_4_z REAL,
    landmark_5_x REAL, landmark_5_y REAL, landmark_5_z REAL,
    landmark_6_x REAL, landmark_6_y REAL, landmark_6_z REAL,
    landmark_7_x REAL, landmark_7_y REAL, landmark_7_z REAL,
    landmark_8_x REAL, landmark_8_y REAL, landmark_8_z REAL,
    landmark_9_x REAL, landmark_9_y REAL, landmark_9_z REAL,
    landmark_10_x REAL, landmark_10_y REAL, landmark_10_z REAL,
    landmark_11_x REAL, landmark_11_y REAL, landmark_11_z REAL,
    landmark_12_x REAL, landmark_12_y REAL, landmark_12_z REAL
)
''')
conexao.commit()