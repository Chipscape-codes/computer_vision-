import Handtrackingmodule as htm
import cv2
import time
import numpy as np 
import keyboard
import time



cap = cv2.VideoCapture(0)
cap.set(3,1288)
cap.set(4,720)

detector = htm.handDetector(detectionCon=0.85)


while True:
    success ,img =cap.read()
    img = cv2.flip(img,1)
    img = detector.findHands(img)
    lmList =detector.findPosition(img ,draw=False)
    
    if len(lmList) > 8 :
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        fingers = detector.fingersUp()
        print(fingers)
        #print(fingers)
        if fingers[1] and fingers[2] and fingers[3] and fingers[4] and fingers[0]:
            cv2.putText(img,"MADHU", (x1,y2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2, cv2.LINE_AA)
            keyboard.press_and_release("m")
            keyboard.press_and_release("a")
            keyboard.press_and_release("d")
            keyboard.press_and_release("h")
            keyboard.press_and_release("u")
            keyboard.press_and_release('space')
            time.sleep(1)
        elif fingers[0]:
            cv2.putText(img,"MY", (x1,y2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2, cv2.LINE_AA)
            keyboard.press_and_release("m")
            keyboard.press_and_release("y")
            keyboard.press_and_release('space')
            time.sleep(1)
        elif fingers[1] :
            cv2.putText(img,"Name", (x1,y2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2, cv2.LINE_AA)
            keyboard.press_and_release("n")
            keyboard.press_and_release("a")
            keyboard.press_and_release("m")
            keyboard.press_and_release("e")
            keyboard.press_and_release('space')
            time.sleep(1)
        elif fingers[4] :
            cv2.putText(img,"is", (x1,y2), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2, cv2.LINE_AA) 
            keyboard.press_and_release("i")
            keyboard.press_and_release("s")
            keyboard.press_and_release('space')
            time.sleep(1)                   
    cv2.imshow("Image",img)
    cv2.waitKey(1)