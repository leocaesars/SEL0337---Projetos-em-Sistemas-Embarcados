# SEL0337

Parte 1: TAG

Nesta atividade, foi proposto o desenvolvimento de um sistema de controle de acesso utilizando a tecnologia RFID (Radio-Frequency Identification) em conjunto com uma Raspberry Pi. O objetivo principal era criar um mecanismo que permitisse a gravação de informações em uma Tag RFID, a leitura dessas informações, e a implementação de um programa em Python que utilizasse esses dados para controlar o acesso a um determinado local. O processo iniciou com a montagem do circuito, conforme a figura abaixo que envolveu a conexão do módulo RFID-RC522 à Raspberry Pi. 

![20231127_152804](https://github.com/LeoCPSyahoo/SEL0337/assets/116130972/319dfda8-c71d-4dda-be9b-c8734c1bc289)

Para facilitar a comunicação, foi habilitada a interface SPI nas configurações da Raspberry Pi, e a biblioteca Python do módulo RFID (mfrc522) foi instalada. Com base nos códigos fornecidos, foi desenvolvido um programa em Python que lia o ID da tag e acionava um LED verde com a mensagem "Acesso Liberado" caso a Tag estivesse cadastrada, ou um LED vermelho com a mensagem "Acesso Negado" caso não estivesse cadastrada.

![20231127_152752](https://github.com/LeoCPSyahoo/SEL0337/assets/116130972/1f3f52dc-3195-4389-b9d6-ec174e2e30e4)

![Photo from Leonardo](https://github.com/LeoCPSyahoo/SEL0337/assets/116130972/159a9391-ea9e-4676-a3aa-4f3956e0fa19)

Parte 2: Câmera

O código implementa um sistema de detecção facial que captura imagens quando rostos são identificados. O LED é utilizado para fornecer feedback visual durante a detecção.

https://github.com/LeoCPSyahoo/SEL0337/assets/116130972/f2b8e95a-d7e9-4120-96e7-161f034e2fe7

![Foto](https://github.com/LeoCPSyahoo/SEL0337/assets/116130972/9ba2867d-b905-49bc-b9c5-fab13bbdc4c1)

Configurações Iniciais e Importações:

-Importa as bibliotecas necessárias, como OpenCV para processamento de imagens, os módulos necessários da Raspberry Pi para a câmera (picamera2), e a biblioteca LED do GPIO.

-Inicializa um objeto LED associado ao pino GPIO 26.

Carregamento do Classificador Haar Cascade:

-Carrega o classificador Haar Cascade treinado para detecção facial. Esse classificador é utilizado para identificar rostos em uma imagem.

-Configuração da Câmera da Raspberry Pi:

-Inicializa a câmera da Raspberry Pi (Picamera2).

-Configura a câmera para criar uma visualização com formato de representação de cores 32 bits “XRGB8888” e resolução de 640x480 pixels.

Loop Principal para Detecção Facial:

-Inicia um loop infinito para captura e detecção de rostos.

-Captura um quadro da câmera.

-Converte a imagem colorida para escala de cinza para facilitar a detecção facial.

Detecção de Rostos:

-Utiliza o classificador Haar Cascade para detectar rostos na imagem em escala de cinza.

-Quando um rosto é detectado, liga o LED associado ao pino GPIO 26.

-Processamento e Armazenamento de Imagens:

-Desenha um retângulo verde ao redor do rosto na imagem original.

-Gera um nome de arquivo único com base no carimbo de data/hora.

-Salva apenas a porção da imagem que contém o rosto detectado como um arquivo JPEG no diretório especificado.

Espera e Desligamento do LED:

-Espera 0.5 segundos para garantir que apenas uma imagem seja capturada por detecção.

-Desliga o LED associado ao pino GPIO 26.

Exibição da Imagem:

-Exibe a imagem com os retângulos desenhados em uma janela com o título "Camera".

Aguarda e Captura Próxima Imagem:

-Aguarda 300 milissegundos antes de continuar o loop e capturar a próxima imagem.


