"""
FelipedelosH
2025
"""
# Application\UseCases\ISaveDebitReport.py
from abc import ABC, abstractmethod

class ISaveDebitReport(ABC):
    @abstractmethod
    def execute(self, path: str, content: str) -> bool:
        pass
