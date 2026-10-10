"""
FelipedelosH
2025
"""
# Application\UseCases\ISaveSchedule24HReport.py
from abc import ABC, abstractmethod

class ISaveSchedule24HReport(ABC):
    @abstractmethod
    def execute(self, path: str, content: str) -> bool:
        pass
