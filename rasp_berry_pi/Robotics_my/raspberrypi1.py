from imutils.video import VideoStream
import numpy as np
import datetime
import argparse
import imutils
import time
import cv2
import io
import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
# Desliga alertas
gpio.setwarnings(False)

gpio.setup(7, gpio.OUT)
 
#pino de ativação do motor A via Rasp 2 
gpio.setup(11, gpio.OUT)
 
# Iniciar Pino 13 como saida - Motor A
gpio.setup(13, gpio.OUT)
 
#Iniciar Pino 15 como saida - Motor A
gpio.setup(15, gpio.OUT)
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
#----------------------
def front():
    gpio.output(18, True)
    gpio.output(13, True)
def right():
    gpio.output(18, True)
    gpio.output(13, False)
def left():
    gpio.output(13, True)
    gpio.output(18, False)
def stop():
    gpio.output(13, False)
    gpio.output(18, False)
def ajustez(area):
    if(area>200):
        front()
    elif(area<=120):
        right()
    else:
        left()

gpio.cleanup()

    

