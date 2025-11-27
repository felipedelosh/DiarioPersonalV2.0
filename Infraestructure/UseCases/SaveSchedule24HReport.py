"""
FelipedelosH
2025
"""
from Application.UseCases.ISaveSchedule24HReport import ISaveSchedule24HReport
from Application.Services.IScheduleService import IScheduleService

class SaveSchedule24HReport(ISaveSchedule24HReport):
    def __init__(self, service: IScheduleService):
        self.feeling_service = service

    def execute(self, path: str, content: str) -> bool:
        return self.feeling_service.save_24h_report(path, content)
