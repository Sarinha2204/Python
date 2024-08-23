import cv2  # pip install opencv-python

# Carregar o classificador em cascata para detecção de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicialize a captura de vídeo
cap = cv2.VideoCapture(1)

while True:
    # Capture frame a frame
    ret, frame = cap.read()

    # Verifique se o frame foi capturado corretamente
    if not ret:
        print("Não foi possível capturar o vídeo")
        break

    # Converter a imagem para escala de cinza (necessário para o classificador em cascata)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostos no frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Desenhar retângulos ao redor dos rostos detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Azul, espessura 2

    # Exiba o frame com os rostos detectados
    cv2.imshow("Imagem", frame)

    # Encerre a captura quando a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere a captura e feche todas as janelas
cap.release()
cv2.destroyAllWindows()
