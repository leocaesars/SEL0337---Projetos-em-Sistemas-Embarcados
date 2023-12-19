# SEL0337

Parte 1: TAG
Nesta atividade, foi proposto o desenvolvimento de um sistema de controle de acesso utilizando a tecnologia RFID (Radio-Frequency Identification) em conjunto com uma Raspberry Pi. O objetivo principal era criar um mecanismo que permitisse a gravação de informações em uma Tag RFID, a leitura dessas informações, e a implementação de um programa em Python que utilizasse esses dados para controlar o acesso a um determinado local. O processo iniciou com a montagem do circuito, conforme a figura abaixo que envolveu a conexão do módulo RFID-RC522 à Raspberry Pi. 

Para facilitar a comunicação, foi habilitada a interface SPI nas configurações da Raspberry Pi, e a biblioteca Python do módulo RFID (mfrc522) foi instalada. Com base nos códigos fornecidos, foi desenvolvido um programa em Python que lia o ID da tag e acionava um LED verde com a mensagem "Acesso Liberado" caso a Tag estivesse cadastrada, ou um LED vermelho com a mensagem "Acesso Negado" caso não estivesse cadastrada.

