"""
FelipedelosH
2025
"""
from Application.Repositories.IScheduleRepository import IScheduleRepository
from Infraestructure.Persistence.FileWriter import FileWriter

class ScheduleRepository(IScheduleRepository):
    def __init__(self):
        self.file_writer = FileWriter()

    def save_24h_report(self, path: str, data: str) -> bool:
        return self.file_writer.saveFile(path, data)
