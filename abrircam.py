import cv2 # pip install opencv-python # pip install opencv_-contrib-python

cap = cv2.VideoCapture(0)

while true:
    _, frame = cap.read()

    cvs2.imshow("Imagem Mil Grau", frame)

    cv2.waitKey(1)