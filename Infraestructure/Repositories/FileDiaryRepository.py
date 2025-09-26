"""
FelipedelosH
2025
"""
from Application.Repositories.IDiaryRepository import IDiaryRepository
from Infraestructure.Persistence.FileWriter import FileWriter

class FileDiaryRepository(IDiaryRepository):
    def __init__(self):
        self.file_writer = FileWriter()

    def save_diary_page(self, path: str, content: str) -> bool:
        return self.file_writer.saveFile(path, content)
