import cv2
from cv2 import waitKey
import time
 


cap = cv2.VideoCapture(0)
cap.set(4 ,640)
cap.set(2,480)
camera = True




face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
while camera == True:
    success, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h),(225,0,0), 2)
        
    cv2.imshow('img', frame)
    cv2.waitKey(1)
    if waitKey(1) & 0xFF==ord('c'):
        break

cap.release()
cv2.destroyAllWindows()






    