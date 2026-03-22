"""
FelipedelosH
2026
"""
from Application.Repositories.IBackuprepository import IBackupRepository
from Infraestructure.Persistence.FileWriter import FileWriter
from Infraestructure.Persistence.FileReader import FileReader
from Domain.Entities.Response import Response

class BackupRepository(IBackupRepository):
    def __init__(self):
        self.file_writer = FileWriter()
        self.file_reader = FileReader()

    def save(self, path: str, content: str) -> bool:
        return self.file_writer.saveFile(path, content)
