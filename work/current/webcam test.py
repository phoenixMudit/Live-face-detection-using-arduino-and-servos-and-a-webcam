import numpy as np
import cv2
import os





cap = cv2.VideoCapture(0)



while True:
    ret,img = cap.read()

    cv2.imshow('video',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break



cap.release()


cv2.destroyAllWindows()