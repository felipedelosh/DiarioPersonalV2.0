"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class ISaveDebitReport(ABC):
    @abstractmethod
    def execute(self, path: str, content: str) -> bool:
        pass
