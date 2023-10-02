import numpy as np
import cv2
import os
import serial,time
from serial import Serial

os.chdir("/Users/muditatrey/Live-facedetection/work/current")

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

ArduinoSerial=serial.Serial('/dev/cu.usbmodem142301',9600,timeout=0.1)
time.sleep(1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, img = cap.read()
    img=cv2.flip(img,1)
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces= faceCascade.detectMultiScale(gray,1.1,6)
    for x,y,w,h in faces:
        
        string='X{0:d}Y{1:d}'.format((x+w//2),(y+h//2))
        print(string)
        ArduinoSerial.write(string.encode('utf-8'))
        
        cv2.circle(img,(x+w//2,y+h//2),2,(0,255,0),2)
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    
    cv2.rectangle(img,(640//2-30,480//2-30),
                 (640//2+30,480//2+30),
                  (255,255,255),3) 
    cv2.imshow('video',img)

    k = cv2.waitKey(3) & 0xff
    if k == 27: 
        break

cap.release()


cv2.destroyAllWindows()