"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class IFeelingRepository(ABC):
    @abstractmethod
    def save_feeling(self, path: str, data: str) -> bool:
        pass
