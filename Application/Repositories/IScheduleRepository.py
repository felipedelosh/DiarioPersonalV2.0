"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class IScheduleRepository(ABC):
    @abstractmethod
    def save_24h_report(self, path: str, data: str) -> bool:
        pass

    @abstractmethod
    def get_24h_report(self, path: str) -> str:
        pass
