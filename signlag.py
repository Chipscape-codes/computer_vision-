import Handtrackingmodule as htm
import cv2
import time
import numpy as np 
import pyttsx3
import time

tell = pyttsx3.init()
cap = cv2.VideoCapture(0)
detector = htm.handDetector(detectionCon=0.85)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) > 8:
        x1, y1 = lmList[8][1:] 
        x2, y2 = lmList[12][1:]  
        fingers = detector.fingersUp()

        h, w, _ = img.shape
        if fingers[0] and fingers[1] and fingers[2] and fingers[3]and fingers[4]:
            print('thank you')
            tell.say("Thank you")
            tell.runAndWait()
            
    cv2.imshow("signlang translator", img)
    cv2.waitKey(1)