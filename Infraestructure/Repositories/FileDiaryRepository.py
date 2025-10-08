"""
FelipedelosH
2025
"""
from Application.Repositories.IDiaryRepository import IDiaryRepository
from Infraestructure.Persistence.FileWriter import FileWriter
from Infraestructure.Persistence.FileReader import FileReader
from Domain.Entities.Response import Response

class FileDiaryRepository(IDiaryRepository):
    def __init__(self):
        self.file_writer = FileWriter()
        self.file_reader = FileReader()

    def save_diary_page(self, path: str, content: str) -> bool:
        return self.file_writer.saveFile(path, content)

    def load_diary_page(self, path: str, keyword: str) -> Response:
        return self.file_reader.getFileDataFromKeyword(path, keyword)
