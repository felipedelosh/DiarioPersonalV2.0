"""
FelipedelosH
2025
"""
# Application\UseCases\IPayDebit.py
from abc import ABC, abstractmethod

class IPayDebit(ABC):
    @abstractmethod
    def execute(self, path: str, content: str, date: str, comment: str, state: str) -> bool:
        pass
