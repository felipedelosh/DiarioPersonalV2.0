"""
FelipedelosH
2025
"""
from Application.Repositories.IScheduleRepository import IScheduleRepository
from Infraestructure.Persistence.FileWriter import FileWriter
from Infraestructure.Persistence.FileReader import FileReader

class ScheduleRepository(IScheduleRepository):
    def __init__(self):
        self.file_writer = FileWriter()
        self.file_reader = FileReader()

    def save_24h_report(self, path: str, data: str) -> bool:
        return self.file_writer.saveFile(path, data)
    
    def get_24h_report(self, path: str) -> str:
        return self.file_reader.getFileDataFromPath(path)
