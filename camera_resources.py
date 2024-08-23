from worksheet import worksheet
from cameras.camera import CameraModel

class Cameras:
    @staticmethod
    def get():
        cameras = worksheet.get_all_records()
        return {'cameras': cameras}

class Camera:
    @staticmethod
    def update_status(camera_id, status):
        camera_encontrada = CameraModel.find_camera(camera_id)
        if camera_encontrada:
            try:
                camera_encontrada.update_camera_status(status)
                camera_encontrada.save_camera()
            except Exception as e:
                print(f"An internal error occurred trying to update camera '{camera_id}' status: {e}")
        else:
            print(f"Camera '{camera_id}' not found.")
