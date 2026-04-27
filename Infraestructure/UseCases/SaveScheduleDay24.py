"""
FelipedelosH
2026
"""
from Application.UseCases.ISaveScheduleDay24 import ISaveScheduleDay24
from Application.Services.IScheduleService import IScheduleService

class SaveScheduleDay24(ISaveScheduleDay24):
    def __init__(self, schedule_service: IScheduleService):
        self.schedule_service = schedule_service

    def execute(self, base_path: str, specify_path, content: str) -> bool:
        _status = self.schedule_service.save_24h_report(base_path, content)
        _status = _status and self.schedule_service.save_24h_report(specify_path, content)
        return _status
