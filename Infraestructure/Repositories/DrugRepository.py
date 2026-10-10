"""
FelipedelosH
2025
"""
from Application.Repositories.IDrugRepository import IDrugRepository
from Infraestructure.Persistence.FileWriter import FileWriter
from Infraestructure.Persistence.FileReader import FileReader
from Domain.Entities.Response import Response

class DrugRepository(IDrugRepository):
    def __init__(self):
        self.file_writer = FileWriter()
        self.file_reader = FileReader()

    def save_drug_usage(self, path: str, content: str) -> bool:
        return self.file_writer.saveFile(path, content)

    def get_drug_info(self, path: str) -> Response:
        return self.file_reader.getFileDataFromPath(path)
