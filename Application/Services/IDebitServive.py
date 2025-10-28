"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class IDebitService(ABC):
    @abstractmethod
    def save_debit_report(self, path: str, content: str) -> bool:
        pass
