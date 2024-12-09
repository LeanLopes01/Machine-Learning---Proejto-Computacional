# Reconhecimento Facial---Proejto-Computacional
Este projeto é um sistema de vigilância residencial com reconhecimento facial, desenvolvido utilizando diversas bibliotecas do Python para oferecer uma solução funcional e intuitiva. Entre as bibliotecas utilizadas estão: **numpy**, para operações matemáticas e manipulação de arrays; **face_recognition**, responsável pelo registro e reconhecimento de rostos; **sqlite3**, utilizada para criar e gerenciar o banco de dados onde as informações dos rostos registrados são armazenadas; **PyQt6**, para o desenvolvimento da interface gráfica com auxílio do **QT Designer**, integrado ao código por meio do arquivo **window.py**; e **opencv**, para captura de imagens em tempo real e processamento.

Para baixar o **face_recognition** deve primeiramente baixar o **CMake** no computador. Site: https://cmake.org/download/
Após baixar o **CMake** vá ao cmd e coloque o seguinte código: pip install face_recognition. Espere baixar e poderá usar o programa.

Antes de iniciar o programa inicie o "createBD.py" para ele criar o banco de dados.

O funcionamento do sistema é simples e prático. Para registrar um rosto, o usuário deve clicar no botão **Registrar Rosto** e inserir seu nome no campo que aparece em um popup. Após isso, o programa capturará a imagem do rosto e a armazenará no banco de dados. O processo leva cerca de 10 segundos, e ao final, uma mensagem de confirmação será exibida, indicando que a imagem foi salva. Além disso, a lista de pessoas registradas será atualizada na aba de texto exibida abaixo da interface.

Uma vez que os rostos estejam registrados, é possível ativar a detecção de suspeitos clicando no botão **Detectar Suspeitos**. O sistema passará a monitorar em tempo real, identificando as pessoas presentes. Quando uma pessoa registrada no banco de dados for reconhecida, o programa exibirá seu nome no terminal. Caso seja detectada uma pessoa que não está registrada, o sistema a marcará como suspeita.

Por fim, para encerrar o programa, o usuário pode simplesmente clicar no botão **Sair**, o que fechará o aplicativo. Este projeto demonstra como a integração de inteligência artificial com interfaces gráficas em Python pode ser utilizada para criar aplicações úteis e acessíveis no dia a dia.
