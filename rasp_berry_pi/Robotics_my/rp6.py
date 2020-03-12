import time
import numpy as np
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
# Desliga alertas
gpio.setwarnings(False)
#---------------------------------------
#Declara pinos como saida GPIO - Motor A
 
#pino de ativação do motor A via Rasp 1
gpio.setup(7, gpio.OUT)
 
#pino de ativação do motor A via Rasp 2 
gpio.setup(11, gpio.OUT)
 
# Iniciar Pino 13 como saida - Motor A
gpio.setup(13, gpio.OUT)
 
#Iniciar Pino 15 como saida - Motor A
gpio.setup(15, gpio.OUT)
 
#---------------------------------------
#Declara pinos como saida GPIO - Motor B
 
#pino de ativação do motor B via Rasp 1
gpio.setup(26, gpio.OUT)
 
#pino de ativação do motor B via Rasp 2 
gpio.setup(16, gpio.OUT)
 
# Iniciar Pino 5 como saida - Motor B
gpio.setup(18, gpio.OUT)
 
#Iniciar Pino 22 como saida - Motor B
gpio.setup(22, gpio.OUT)
gpio.output(7, True) #Motor A - Rasp 1
gpio.output(11, True) #Motor A - Rasp 2
#---------------------------------------
#Valores iniciais - True - Motor B ativado
gpio.output(26, True) #Motor B - Rasp 1
gpio.output(16, True) #Motor B - Rasp 2

def Frente():
# Motor 1
 gpio.output(13, True)
 gpio.output(15, False)
# Motor 2
 gpio.output(18, False)
 gpio.output(22, True)
	
def Tras():
# Motor 1
 gpio.output(13, False)
 gpio.output(15, True)
# Motor 2
 gpio.output(18, True)
 gpio.output(22, False)
def Parar():
# Motor 1
 gpio.output(18, False)
 gpio.output(22, False)
# Motor 2
 gpio.output(13, False)
 gpio.output(15, False)


def Direita():
# Motor 1
 gpio.output(13, True)
 gpio.output(15, False)
# Motor 2
 gpio.output(18, True)
 gpio.output(22, False)


def Esquerda():
# Motor 1
 gpio.output(13, False)
 gpio.output(15, True)
# Motor 2
 gpio.output(18, False)
 gpio.output(22, True)
