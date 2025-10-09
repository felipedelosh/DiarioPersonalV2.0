"""
FelipedelosH
2025
"""
from Application.Repositories.IFeelingRepository import IFeelingRepository
from Infraestructure.Persistence.FileWriter import FileWriter

class FeelingRepository(IFeelingRepository):
    def __init__(self):
        self.file_writer = FileWriter()

    def save_feeling(self, path: str, data: str) -> bool:
        return self.file_writer.saveFile(path, data)