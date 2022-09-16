# Importar a biblioteca OpenCV para usar Visão Computacional
from pyexpat import model
import cv2
# Importar MediaPipe para utilizar a função hands
import mediapipe as mp
# Importar para o utilizar o TensorFlow
from keras.models import load_model
# from keras import models    
# model = models.load_model('keras_model.h5')
import numpy as np

# Tensorflow deve estar na versão 2.9.1 para não ter problema de incompatibilidade

# Abertura e captura do vídeo onde o parâmetro 0 é a câmera que será aberta
video = cv2.VideoCapture(0)

# Variável de configuração do MediaPipe pra utilizar a função hands e fazer o mapeamento/detecção
#  das mãos dentro do vídeo com max_num_hands=1 para apenas uma mão se quiser mais aumentar o número
hands = mp.solutions.hands.Hands(max_num_hands=1)

# Array que vai receber as labels ou título de cada classe do dataset na mesma ordem que elas 
# foram criadas pois cada posição desse array é um número que será utilizado na predição final
classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# Importando o modelo criado no site Teachable machine passando o nome dele como parâmetro
model = load_model('keras_model.h5')
# Definindo o array de entrada
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Criando um loop infinito
while True:
    # Lendo as imagens geradas no vídeo e atribuindo às variáveis check e img
    check, img = video.read()
    # A imagem recebida da câmera vem no formato BGR aqui ela é convertida para RGB para ser processada pelo MediaPipe
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Processando a imagem da mão com MediaPipe
    results = hands.process(imgRGB)
    # Extraindo informações ou coordenadas dos pontos da imagem da mão
    handsPoints = results.multi_hand_landmarks
    # Pegando as dimensões da imagem da mão com as variáveis h de height(altura), w de width(largura) e a 3ª variável não precisa
    h, w, _ = img.shape

    # Essa condicional só será exacutada se a variável handPoints não estiver vazia
    # Ela serve para checar se existe mesmo a mão na imagem, caso contrário, o modelo treinado não será processado  
    # Ela também faz com que a mão seja identificada dentro da imagem devolvendo a informação de onde ela se encontra na imagem
    if handsPoints != None:
        # Criando um bounding box (retângulo) ao redor da mão extraindo as dimensões que formam um retângulo
        # Essa função não é nativa no MediaPipe havendo a necessidade de criação da lógica para extrair as informações 
        for hand in handsPoints:
            x_max = 0
            y_max = 0
            x_min = w
            y_min = h
            # for para enumerar as landmarks (pontos da mão) e atribuir essa numeração à variável lm 
            for lm in hand.landmark:
                # Fazendo a conversão dos landmarks(pontos da mão) em pixels
                x, y = int(lm.x * w), int(lm.y * h)
                if x > x_max:
                    x_max = x
                if x < x_min:
                    x_min = x
                if y > y_max:
                    y_max = y
                if y < y_min:
                    y_min = y
            # Criando o desenho do retângulo
            cv2.rectangle(img, (x_min-50, y_min-50), (x_max+50, y_max+50), (0, 255, 0), 2)

            try:
                # Fazendo um corte da imagem na mesma posição do retângulo, separando da imagem apenas a mão, para o modelo fazer a predição
                imgCrop = img[y_min-50:y_max+50,x_min-50:x_max+50]
                # redimensionar a imagem
                imgCrop = cv2.resize(imgCrop,(224,224))
                # Transformar a imagem num array
                imgArray = np.asarray(imgCrop)
                # Fazer a normalização da imagem
                normalized_image_array = (imgArray.astype(np.float32) / 127.0) - 1
                data[0] = normalized_image_array
                # Predição com a probabilidade da imagem conter cada uma das classes (números em libras)
                prediction = model.predict(data)
                # Índice com cada classe representando um número e extraindo-se a maior probabilidade da classe/índice/número mais predominante na imagem
                indexVal = np.argmax(prediction)
                #print(classes[indexVal])
                cv2.putText(img,classes[indexVal],(x_min-50,y_min-65),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,255),5)

            except:
                continue

    cv2.imshow('Imagem',img)
    cv2.waitKey(1)