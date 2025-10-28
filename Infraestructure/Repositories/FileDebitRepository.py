"""
FelipedelosH
2025
"""
from Application.Repositories.IDebitRepository import IDebitRepository
from Infraestructure.Persistence.FileWriter import FileWriter
from Infraestructure.Persistence.FileReader import FileReader
from Domain.Entities.Response import Response

class FileDebitRepository(IDebitRepository):
    def __init__(self):
        self.file_writer = FileWriter()
        self.file_reader = FileReader()

    def save_debit_report(self, path: str, content: str) -> bool:
        return self.file_writer.saveFile(path, content)