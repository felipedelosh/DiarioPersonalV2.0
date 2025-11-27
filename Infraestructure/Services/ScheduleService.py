"""
FelipedelosH
2025
"""
from Application.Services.IScheduleService import IScheduleService
from Application.Repositories.IScheduleRepository import IScheduleRepository
from Domain.Entities.Response import Response

class ScheduleService(IScheduleService):
    def __init__(self,  schedule_repo: IScheduleRepository):
        self.schedule_repo = schedule_repo

    def save_24h_report(self, path: str, content: str) -> bool:
        return self.schedule_repo.save_24h_report(path, content)
