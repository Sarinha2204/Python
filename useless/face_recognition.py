import cv2
import useless.face_recognition as face_recognition

# Carregar imagem conhecida e obter a codificação facial
known_image = face_recognition.load_image_file("known_person.jpg")
known_face_encoding = face_recognition.face_encodings(known_image)[0]

# Lista de codificações faciais conhecidas e seus nomes
known_face_encodings = [known_face_encoding]
known_face_names = ["Nome da Pessoa"]

# Abrir o arquivo de vídeo
video_capture = cv2.VideoCapture("video.mp4")

while True:
    # Captura frame a frame
    ret, frame = video_capture.read()

    # Se o frame foi capturado corretamente
    if not ret:
        print("Fim do vídeo ou erro na captura do frame.")
        break

    # Converte o frame para RGB (face_recognition usa RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Encontra todos os rostos no frame e suas codificações
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Verifica se o rosto encontrado corresponde a algum rosto conhecido
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Desconhecido"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Desenha um retângulo ao redor do rosto e coloca o nome
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

    # Exibe o frame com os rostos detectados e reconhecidos
    cv2.imshow('Video', frame)

    # Sai do loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libere o vídeo e feche todas as janelas
video_capture.release()
cv2.destroyAllWindows()
