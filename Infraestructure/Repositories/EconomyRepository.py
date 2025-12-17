"""
FelipedelosH
2025
"""
from Application.Repositories.IEconomyRepository import IEconomyRepository
from Infraestructure.Persistence.FileWriter import FileWriter
from Infraestructure.Persistence.FileReader import FileReader
from Domain.Entities.Response import Response

class FileEconomyRepository(IEconomyRepository):
    def __init__(self):
        self.file_writer = FileWriter()
        self.file_reader = FileReader()

    def save_economy_taccount_report(self, path: str, content: str) -> bool:
        return self.file_writer.saveFile(path, content)

    def update_economy_taccount_report(self, path: str, content: str) -> bool:
        return self.file_writer.overWritefile(path, content)

    def get_economy_taccount_report(self, path: str) -> Response:
        return self.file_reader.getFileDataFromPath(path)
