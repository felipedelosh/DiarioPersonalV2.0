"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IScheduleService(ABC):
    @abstractmethod
    def save_24h_report(self, path: str, content: str) -> bool:
        pass
