"""
FelipedelosH
2025
"""
# Application\UseCases\ISaveEconomyTAccountReport.py
from abc import ABC, abstractmethod

class ISaveEconomyTAccountReport(ABC):
    @abstractmethod
    def execute(self, path: str, content: str) -> bool:
        pass
