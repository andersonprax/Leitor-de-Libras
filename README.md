# Leitor-de-Libras

TCC - TRABALHO DE CONCLUSÃO DA RESIDÊNCIA EM ROBÓTICA E INTELIGÊNCIA ARTIFICIAL APLICADAS A TESTE DE SOFTWARE - CENTRO DE INFORMÁTICA - CIn DA UNIVERSIDADE FEDERAL DE PERNAMBUCO - UFPE

 App que identifica os gestos das mãos traduzindo-os em Língua Brasileira de Sinais - Libras. Esse app usa TensorFlow | IA | Deep Learning | Redes Neurais | Visão Computacional | Teachable Machine.

 Foi utilizado apenas números em libras para que a aplicação seja capaz de identificar e aprender os mesmos, a fim de que sejam digitados no terminal e urna eletrônica por um braço robótico, sendo esses a princípio simulados no programa CoppeliaSim.

 Primeiramente foi criado um novo projeto do tipo imagem no site: https://teachablemachine.withgoogle.com/. Foi utilizado a primeira opção padrão do projeto de imagem que é 224 x 224. Nesse projeto, foram criadas classes, sendo cada uma correspondente a um número e contendo as imagens das mãos, direita e esquerdas, reproduzindo os gestos dos números em libras. Essas imagens foram capturadas através da webcam do notebook durante 6 (seis) segundos, gerando um dataset com um total de 3549 imagens como se pode notar nesta tabela:     Classes	    Quantidade de imagens
                "0"         	     294
                "1"	              543
                "2"	              268
                "3"	              264
                "4"	              267
                "5"	              265
                "6"	              552
                "7"	              271
                "8"	              266
                "9"	              559

Logo após foi feito o treinamento do modelo com o dataset das imagens, clicando-se no botão training onde a aplicação online Teachable Machine mostra alguns dados como a quantidade de épocas, batch size (tamanho de lote), learning rate (taxa de aprendizado)

No próprio site pode-se ver um exemplo da acurácia/assertividade dos modelos, posicionando-se as mãos na amostra do vídeo da webcam no site e fazendo-se os gestos dos números em libras para que o software possa dizer quais números são mostrados.  

Deve-se exportar o modelo para ser utilizado no projeto clicando-se no botão Export Model, seleciona-se a opção Tensorflow, deixar marcado a opção Keras e fazer o download do modelo. Na pasta do modelo baixado, tem-se o modelo propriamente dito que se encontra no formato .h5 e as labels contendo os títulos das classes, sendo que somente o modelo (keras_model.h5) será usado no projeto, sendo este então copiado da pasta de origem e colado dentro da pasta do projeto.

Na pasta do projeto tem o arquivo em python leitorLibras.py contendo as importações da biblioteca OpenCV, do MediaPipe onde será utilizada a função hands, do Keras.models para o utilizar o TensorFlow (na última versão que é a 2.9.1) que já vem o com ele instalado e da biblioteca de código aberto que auxilia em operações matemáticas complexas chamada numpy. Para reproduzir esse projeto ou usá-lo em outros futuros, é de suma importância que a versão do Tensorflow seja a mesma que a mencionada anteriormente para que não haja problemas de incompatibilidade.

Para realizar este projeto deve-se seguir o seguinte fluxo:

1 - Clonar o repositório: Leitor-de-Libras.

2 - Abrir a pasta do repositório clonado.

3 - Abrir o arquivo(cena com simulação do CoppeliaSim): MontagemUrnaeNiryo.ttt

4 - No CoppeliaSim apertar o botão: Start/resume simulation.

5 - Abrir uma IDE para a linguagem python de sua preferência.

6 - Na IDE deve-se abrir a pasta do repositório clonado.

7 - Abrir o arquivo: leitorLibras.py

8 - Importar as bibliotecas necessárias.

9 - Apertar o botão play/run da IDE utilizada.

10 - Abrirá o terminal da IDE e a câmera do device utilizado.

11 - Reproduzir com as mãos gestos de números em libras.

12 - O número será identificado e traduzido.

13 - Será mostrando o número na janela da câmera.

14 - deve-se apertar o botão k do teclado para capturar e armazenar o número.

15 - Deve-se repetir os passos de 12 a 15 mais dez vezes.

16 - Serão capturados e mostrados os 11 números do título de eleitor no terminal da IDE.

17 - No CoppeliaSim o robô NiryoOne se moverá para a posição de segurança.

18 - O braço robótico se moverá para a identificação do mesário.

19 - O braço do robô se moverá para a identificação do eleitor.

20 - Na terminal da IDE aparecerá as informações: "Identificação do mesário", "Identificação do eleitor" e "Realizando identificação..."

21 - No CoppeliaSim o robô então digitará todos os 11 números do título de eleitor no terminal simulado do mesário.

22 - Cada número digitado no CoppeliaSim será mostrado no terminal da IDE.

23 - Ao digitar todos os 11 dígitos o braço do robô se moverá para a posição de segurança.

24 - No terminal da IDE aparecerá uma mensagem para o usuário indicar se deseja corrigir ou não os números digitados: "O título de eleitor esta correto?" "deseja corrigir? Digite s para sim ou n para não: "

25 - Caso seja digitado "s" (opção  sim), o robô clica no botão "CORRIGE" do terminal do mesário e o fluxo volta para o passo 11.

26 - Caso seja digitado "n" (opção não), o robô clica no botão "CONFIRMA" do terminal do mesário.

27 - Por fim, no terminal da IDE aparecerá a mensagem: "Identificação realizada, obrigado!".

