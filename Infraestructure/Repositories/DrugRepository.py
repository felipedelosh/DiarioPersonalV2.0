"""
FelipedelosH
2025
"""
from Application.Repositories.IDrugRepository import IDrugRepository
from Infraestructure.Persistence.FileWriter import FileWriter

class DrugRepository(IDrugRepository):
    def __init__(self):
        self.file_writer = FileWriter()

    def save_drug_usage(self, path: str, content: str) -> bool:
        return self.file_writer.saveFile(path, content)