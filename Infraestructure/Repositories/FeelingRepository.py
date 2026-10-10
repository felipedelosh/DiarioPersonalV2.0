"""
FelipedelosH
2025
"""
from Application.Repositories.IFeelingRepository import IFeelingRepository
from Infraestructure.Persistence.FileWriter import FileWriter
from Infraestructure.Persistence.FileReader import FileReader
from Domain.Entities.Response import Response

class FeelingRepository(IFeelingRepository):
    def __init__(self):
        self.file_writer = FileWriter()
        self.file_reader = FileReader()

    def save_feeling(self, path: str, data: str) -> bool:
        return self.file_writer.saveFile(path, data)

    def get_feel_info(self, path: str) -> Response:
        return self.file_reader.getFileDataFromPath(path)
