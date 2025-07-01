import cv2
import cv2.data
cap =  cv2.VideoCapture(0)
facecascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


while True:
    success , img = cap.read()
    faces = facecascade.detectMultiScale(img, 1.3, 5)
    
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        faces = str(faces)
        cv2.putText(img,faces,(0,0),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("face",img)    
    cv2.waitKey(1)