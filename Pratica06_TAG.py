from mfrc522 import SimpleMFRC522
from time import sleep
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

red = LED(19)
green = LED(16)

leitor = SimpleMFRC522()

print ("Aproxime a tag do leitor para leitura")

while True:
	id,texto = leitor.read()
	if id == 712936067078:
		green.on()
		red.off()
		print("Acesso liberado")
	else:
		green.off()
		red.on()
		print("Acesso negado")
	sleep(2)
