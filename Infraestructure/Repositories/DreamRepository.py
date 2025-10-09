"""
FelipedelosH
2025
"""
from Application.Repositories.IDreamRepository import IDreamRepository
from Infraestructure.Persistence.FileWriter import FileWriter

class FileDreamRepository(IDreamRepository):
    def __init__(self):
        self.file_writer = FileWriter()

    def save_dream_page(self, path: str, content: str) -> bool:
        return self.file_writer.saveFile(path, content)
