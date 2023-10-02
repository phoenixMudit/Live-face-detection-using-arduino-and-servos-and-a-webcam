import threading
import cv2
from cv2 import VideoCapture
from cv2 import waitKey
from deepface import DeepFace
import os
os.chdir("/Users/muditatrey/Live-facedetection/work/current")


cap = cv2.VideoCapture(0)


cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
 
face_match = False

reference_img = cv2.imread("reference.jpg")


def check_face(frame):
    global gace_match
    try:
        if DeepFace.verify(frame, reference_img.copy())['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:
        face_match = False


while True:
    ret, frame = cap.read()
    if ret:
        if counter % 60 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()
            except ValueError:
                pass

        counter+=1

        if face_match:
            cv2.putText(frame, "MATCH!", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)
        else:
            cv2.putText(frame, "NO MATCH!", (20,450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3)

        cv2.imshow("video",frame)


    key = cv2.waitKey(1)
    if key == ord("q"):
        break


cv2.destroyAllWindows()
