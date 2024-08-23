from datetime import datetime
from worksheet import worksheet

class CameraModel:
    def __init__(self, id, nome, status, url, bloco, descricao, ultima_atualizacao):
        self.id = id
        self.nome = nome
        self.status = status
        self.url = url
        self.bloco = bloco
        self.descricao = descricao
        self.ultima_atualizacao = ultima_atualizacao

    @classmethod
    def from_map(cls, row):
        return cls(**row)
    
    def to_map(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'status': self.status,
            'url': self.url,
            'bloco': self.bloco,
            'descricao': self.descricao,
            'ultima_atualizacao': self.ultima_atualizacao
        }
    
    @staticmethod
    def find_camera(camera_id):
        try:
            camera_row = worksheet.find(f"{camera_id}").row
            dados = worksheet.row_values(camera_row)
            if dados:
                return CameraModel.from_map(dict(zip(['id', 'nome', 'status', 'url', 'bloco', 'descricao', 'ultima_atualizacao'], dados)))
        except Exception as e:
            print(f"Error finding camera: {e}")
        return None
    
    def update_camera_status(self, status):
        DATE_FORMAT = "%d/%m/%Y - %H:%M"
        date = datetime.now().strftime(DATE_FORMAT)
        self.status = status
        self.ultima_atualizacao = date

    def save_camera(self):
        try:
            camera_row = worksheet.find(f"{self.id}").row
            values = [self.id, self.nome, self.status, self.url, self.bloco, self.descricao, self.ultima_atualizacao]
            worksheet.update(f"A{camera_row}:G{camera_row}", [values])
        except Exception as e:
            print(f"Error saving camera: {e}")
    
    def delete_camera(self):
        pass
