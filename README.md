# Reconhecimento Facial---Proejto-Computacional
As bibliotecas usadas no projeto foram: numpy, face_recognition, sqlite3, PyQt6, opencv

O programa utiliza o face_recognition para registrar o rosto do usuário e salva-lo em uma banco de dados feito pelo sqlite3, feito isso você pode deixar para detectar suspeitos (pessoas não registradas no banco de dados)

Com o PyQt6 foi feito uma interface usando o QT Designer e transformado no window.py que faz todo o código funcionar. 

Para utilizar o programa deve primeiramente clicar em Registrar Rosto e inserir seu nome no campo popup que abrir. Espere cerca de 10 segundos até aparecer a mensagem que a imagem foi salva, na aba de texto abaixo irá aparecer as pessoas registradas. Após isso clique em detectar suspeitos e isso vai rodar o código que toda vez que ver alguem que está salvo no banco de dados irá responder no print. No botão sair o aplicativo fecha.
