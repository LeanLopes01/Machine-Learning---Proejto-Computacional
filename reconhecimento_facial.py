''' 
Aqui é o código que faz todas as landmarcks dos rostos que ficam na frente da câmera, ele pega todas as landmarck registradas
no arquivo de bancoDeDados.py e importa os rostos já registrados no banco de dados
''''

import sys
import face_recognition
import cv2
import numpy as np
import bancoDeDados as bd
import json
import window as w

wd = w.Janela_Principal()

class Reconhecimento:

    def __init__(self, nome):
        self.cap = None
        self.timer = None
        self.nome = nome
    
    def capturar_rosto_autorizado(self):
        self.cap = cv2.VideoCapture(0)
        print("Instruções: Aproxime o rosto autorizado da câmera")
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print(self, "Erro", "Erro ao capturar o vídeo.")
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_frame)

            if face_locations:
                face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
                if face_encodings:
                    data = face_encodings[0].tolist()
                    register = bd.RegistroBD(self.nome, data)
                    register.registrar_reconhecimento()
                    print(self, "Sucesso", "Rosto autorizado capturado e salvo com sucesso.")
                    break

            self.update_video_frame(frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break

        self.cap.release()
        self.cap = None

    def detectar_suspeitos(self):
        try:
            ### obter todas as pessoas permitidas do banco de dados ###
            sb = bd.SelecaoTodosNomes()
            pessoas_autorizadas = sb.SelecionarTodosNomes()

            if not pessoas_autorizadas:
                print(self, "Informação", "Nenhum rosto autorizado encontrado no banco de dados.")
                return

            codificacoes_autorizadas = []
            nomes_autorizados = []
            for pessoa in pessoas_autorizadas:
                nomes_autorizados.append(pessoa["nome"])
                codificacoes_autorizadas.append(np.array(pessoa["face_encoding"]))

            ### iniciar captura de vídeo ###
            self.cap = cv2.VideoCapture(0)
            print(self, "Instruções", "Verificando rostos... Pressione 'q' para sair.")

            while True:
                ret, frame = self.cap.read()
                if not ret:
                    print(self, "Erro", "Erro ao capturar o vídeo.")
                    break

                ### detectar rostos no quadro atual ###
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                face_locations = face_recognition.face_locations(rgb_frame)
                face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

                for face_encoding, face_location in zip(face_encodings, face_locations):
                    # Comparar rosto detectado com os rostos autorizados
                    results = face_recognition.compare_faces(codificacoes_autorizadas, face_encoding)
                    distances = face_recognition.face_distance(codificacoes_autorizadas, face_encoding)

                    if True in results:
                        # Identificar a pessoa com a menor distância
                        index = np.argmin(distances)
                        nome = nomes_autorizados[index]
                        mensagem = f"Rosto autorizado detectado: {nome}. Distância: {distances[index]:.4f}"
                    else:
                        mensagem = "Suspeito detectado! Nenhum rosto correspondente encontrado."

                    ### exibir mensagem no console ou interface ###
                    print(mensagem)

                ### atualizar o feed de vídeo na interface (se aplicável) ###
                self.update_video_frame(frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        except Exception as e:
            print(self, "Erro", f"Ocorreu um erro: {e}")

        finally:
            if self.cap:
                self.cap.release()
                self.cap = None

    def update_video_frame(self, frame):
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        #qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        #self.video_label.setPixmap(QPixmap.fromImage(qt_image))
