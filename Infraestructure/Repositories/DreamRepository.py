"""
FelipedelosH
2025
"""
from Application.Repositories.IDreamRepository import IDreamRepository
from Infraestructure.Persistence.FileWriter import FileWriter
from Infraestructure.Persistence.FileReader import FileReader
from Domain.Entities.Response import Response

class FileDreamRepository(IDreamRepository):
    def __init__(self):
        self.file_writer = FileWriter()
        self.file_reader = FileReader()

    def save_dream_page(self, path: str, content: str) -> bool:
        return self.file_writer.saveFile(path, content)
    
    def load_dream_page(self, path: str, keyword: str) -> Response:
        return self.file_reader.getFileDataFromKeyword(path, keyword)
