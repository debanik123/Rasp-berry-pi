import time
 
import cv2
import numpy as np
from imutils.video import VideoStream
import imutils
import math
import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 16
Motor1B = 18
Motor1E = 22
 
Motor2A = 23
Motor2B = 21
Motor2E = 19
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)
usingPiCamera = True
frameSize = (640,480)
vs = VideoStream(src=0, usePiCamera=usingPiCamera, resolution=frameSize,
		framerate=32).start()
time.sleep(2.0)
timeCheck = time.time()
while True:
    img = vs.read()
    if not usingPiCamera:
        img = imutils.resize(img, width=frameSize[0])
    cv2.rectangle(img,(300,300),(100,100),(0,255,0),0)
    crop_img = img[100:300, 100:300]
    grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    value = (35, 35)
    blurred = cv2.GaussianBlur(grey, value, 0)
    _, thresh1 = cv2.threshold(blurred, 127, 255,
                               cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imshow('Thresholded', thresh1)
    contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE,             cv2.CHAIN_APPROX_NONE)
    max_area = -1
    for i in range(len(contours)):
        cnt=contours[i]
        area = cv2.contourArea(cnt)
        if(area>max_area):
            max_area=area
            ci=i
    cnt=contours[ci]
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(crop_img,(x,y),(x+w,y+h),(0,0,255),0)
    hull = cv2.convexHull(cnt)
    drawing = np.zeros(crop_img.shape,np.uint8)
    cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
    cv2.drawContours(drawing,[hull],0,(0,0,255),0)
    hull = cv2.convexHull(cnt,returnPoints = False)
    defects = cv2.convexityDefects(cnt,hull)
    count_defects = 0
    cv2.drawContours(thresh1, contours, -1, (0,255,0), 3)
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(cnt[s][0])
        end = tuple(cnt[e][0])
        far = tuple(cnt[f][0])
        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
        if angle <= 90:
            count_defects += 1
            cv2.circle(crop_img,far,1,[0,0,255],-1)
        #dist = cv2.pointPolygonTest(cnt,far,True)
        cv2.line(crop_img,start,end,[0,255,0],2)
        #cv2.circle(crop_img,far,5,[0,0,255],-1)
    if count_defects == 1:
        cv2.putText(img,"I'M Debanik Roy", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        print("Going forword")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor1E,GPIO.LOW)
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.HIGH)
        GPIO.output(Motor2E,GPIO.LOW)
    
    elif count_defects == 2:
        str = "THIS IS A BASIC HAND GESTURE RECOGNISER!!"
        cv2.putText(img, str, (5,50), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
        print("Going backword")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)
        
    elif count_defects == 3:
        cv2.putText(img,"This is three (:", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        print("Going left")
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor1E,GPIO.LOW)
        GPIO.output(Motor2A,GPIO.LOW)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)
    

        
    elif count_defects == 4:
        cv2.putText(img,"HARE ROBOT", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        print("Going right")
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor1E,GPIO.LOW)
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.HIGH)
        GPIO.output(Motor2E,GPIO.LOW)
        
    else:
        cv2.putText(img,"GOOD AFTERNOON TEACHERS", (50,50),cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        GPIO.output(Motor1A,GPIO.LOW)
        GPIO.output(Motor2A,GPIO.LOW)
        
    #cv2.imshow('drawing', drawing)
    #cv2.imshow('end', crop_img)
    cv2.imshow('Gesture', img)
    all_img = np.hstack((drawing, crop_img))
    cv2.imshow('Contours', all_img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    print(1/(time.time() - timeCheck))
    timeCheck = time.time()
cv2.destroyAllWindows()
GPIO.cleanup()
vs.stop()

