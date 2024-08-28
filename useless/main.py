from threading import Thread
from cameras.camera import CameraModel
from cameras.camera_resources import Cameras
from cameras.camera_operations import start_camera

def main():
    data = Cameras.get()['cameras']
    cameras = [CameraModel.from_map(row) for row in data]
    threads = [Thread(target=start_camera, args=(camera,)) for camera in cameras]
    for thread in threads:
        thread.start()

if __name__ == "__main__":
    main()
