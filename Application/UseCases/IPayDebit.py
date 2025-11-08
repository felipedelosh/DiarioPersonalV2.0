"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class IPayDebit(ABC):
    @abstractmethod
    def execute(self, path: str, content: str, date: str, comment: str, state: str) -> bool:
        pass
