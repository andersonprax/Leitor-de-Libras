# Leitor-de-Libras
 App que identifica os gestos das mãos traduzindo-os em Língua Brasileira de Sinais - Libras. Esse app usa TensorFlow | IA | Deep Learning | Redes Neurais | Visão Computacional | Teachable Machine.

 Foi utilizado apenas números em libras para que a aplicação seja capaz de identificar e aprender os mesmos, a fim de que sejam digitados no terminal e urna eletrônica por um braço robótico, sendo esses a princípio simulados no programa CoppeliaSim.

 Primeiramente foi criado um novo projeto do tipo imagem no site: https://teachablemachine.withgoogle.com/. Foi utilizado a primeira opção padrão do projeto de imagem que é 224 x 224. Nesse projeto, foram criadas classes, sendo cada uma correspondente a um número e contendo as imagens das mãos, direita e esquerdas, reproduzindo os gestos dos números em libras. Essas imagens foram capturadas através da webcam do notebook durante 6 (seis) segundos, gerando um dataset com um total de 3549 imagens como se pode notar nesta tabela:     Classes	    Quantidade de imagens
                "0"         	  294
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

