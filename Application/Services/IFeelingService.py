"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class IFeelingService(ABC):
    @abstractmethod
    def save_feeling(self, path: str, content: str) -> bool:
        pass