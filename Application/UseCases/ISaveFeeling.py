"""
FelipedelosH
2025
"""
# Application\UseCases\ISaveFeeling.py
from abc import ABC, abstractmethod

class ISaveFeeling(ABC):
    @abstractmethod
    def execute(self, path: str, content: str) -> bool:
        pass
