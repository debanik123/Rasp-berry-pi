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
#---------------------------------------

def Frente():
    # Motor 1
    #front
    gpio.output(13, True)
    gpio.output(15, False)
    # Motor 2
    gpio.output(18, False)
    gpio.output(22, True)
	
def Tras():
    #after
    #Motor 1
    gpio.output(13, False)
    gpio.output(15, True)
    # Motor 2
    gpio.output(18, True)
    gpio.output(22, False)
def Parar():
    #stop
    # Motor 1
    gpio.output(18, False)
    gpio.output(22, False)
    # Motor 2
    gpio.output(13, False)
    gpio.output(15, False)


def Direita():
    # Motor 1
    #right
    gpio.output(13, True)
    gpio.output(15, False)
    # Motor 2
    gpio.output(18, True)
    gpio.output(22, False)

def Esquerda():
    # Motor 1
    #left
    gpio.output(13, False)
    gpio.output(15, True)
    # Motor 2
    gpio.output(18, False)
    gpio.output(22, True)

 
def ajusteZ(area):
    if(area<=120):
      Frente()
    elif(area>=600):
        Tras()
    else:
        Parar()
	  
    
    
      
minArea = 50

rangeMin = np.array([42,62,63],np.uint8)
rangeMax = np.array([92,255,235],np.uint8)
usingPiCamera = True

frameSize = (160,128)
vs = VideoStream(src=0, usePiCamera=usingPiCamera,resolution=frameSize,framerate=32).start()

time.sleep(2.0)

while True:
    frame = vs.read()
    if not usingPiCamera:
        frame = imutils.resize(frame,width=frameSize[0])

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    imgThresh = cv2.inRange(hsv,rangeMin,rangeMax)
    imgErode = cv2.erode(imgThresh,None,iterations=3)
    moments = cv2.moments(imgErode,True)
    area = moments["m00"]
    

    if moments["m00"] >= minArea:
        print(area)
        ajusteZ(area)
    else:
        Parar()
        
        
    
	

    
        
cv2.DestroyAllWindows()
gpio.cleanup()
cap.release()
    
