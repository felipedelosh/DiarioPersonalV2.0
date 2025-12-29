"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class IMakeDebtPayment(ABC):
    @abstractmethod
    def execute(self, path: str, content: str, amount: float, date: str, comment: str) -> bool:
        pass
