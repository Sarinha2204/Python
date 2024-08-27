import cv2

# Carregar o classificador em cascata para detecção de rostos
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicialize a captura de vídeo
cap = cv2.VideoCapture(0)

# Lista para armazenar rostos detectados
previous_faces = []
count = 0

while True:
    # Capture frame a frame
    ret, frame = cap.read()

    # Verifique se o frame foi capturado corretamente
    if not ret:
        print("Não foi possível capturar o vídeo")
        break

    # Converter a imagem para escala de cinza
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostos no frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Criar uma lista para armazenar rostos que ainda estão visíveis
    current_faces = []

    # Adicionar rostos detectados ao frame e atualizar a lista de rostos visíveis
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Azul, espessura 2
        current_faces.append((x, y, w, h))

    # Verificar se os rostos detectados são novos e não estavam na lista anterior
    for (x, y, w, h) in current_faces:
        if not any(abs(x - px) < 50 and abs(y - py) < 50 for (px, py, pw, ph) in previous_faces):
            count += 1

    # Atualizar a lista de rostos detectados
    previous_faces = current_faces

    # Mostrar o contador de pessoas
    cv2.putText(frame, f'Contagem: {count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Exibir o frame com os rostos detectados e a contagem
    cv2.imshow("Imagem", frame)

    # Encerre a captura quando a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere a captura e feche todas as janelas
cap.release()
cv2.destroyAllWindows()
