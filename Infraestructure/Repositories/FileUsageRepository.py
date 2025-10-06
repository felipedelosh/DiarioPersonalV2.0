"""
FelipedelosH
2025
"""
from Application.Repositories.IUsageRepository import IUsageRepository
from Infraestructure.Persistence.FileWriter import FileWriter

class FileUsageRepository(IUsageRepository):
    def __init__(self):
        self.file_writer = FileWriter()

    def save_usage(self, path: str, data: str) -> bool:
        return self.file_writer.saveUsage(path, data)
