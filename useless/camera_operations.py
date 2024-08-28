import cv2
import time
import statistics
from cameras.camera import Camera

def start_camera(camera):
    print(f"Starting {camera.nome}")

    while True:
        capture = cv2.VideoCapture(camera.url)
        if not capture.isOpened():
            Camera.update_status(camera.id, "Sem sinal")
            time.sleep(30)
            continue
        
        ret, _ = capture.read()
        if not ret:
            Camera.update_status(camera.id, "Offline")
        else:
            if check_freezing(capture):
                Camera.update_status(camera.id, "Erro")
            else:
                Camera.update_status(camera.id, "Online")
        time.sleep(1)

def check_freezing(capture, intervalo_minutos=0.2):
    tempo_inicial = time.time()
    frames = []
    is_freezing = []

    while time.time() - tempo_inicial < intervalo_minutos * 60:
        ret, frame = capture.read()
        if not ret:
            continue
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frames.append(gray_frame)
        time.sleep(0.1)

    for i, frame in enumerate(frames):
        for j in range(i + 1, len(frames)):
            norm_diff = cv2.norm(frame, frames[j])
            is_freezing.append(norm_diff < 2000)

    if is_freezing:
        mode = statistics.mode(is_freezing)
        return mode
    return False
