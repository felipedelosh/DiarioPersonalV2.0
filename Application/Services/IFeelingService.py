"""
FelipedelosH
2025
"""
# Application\Services\IFeelingService.py
from abc import ABC, abstractmethod

class IFeelingService(ABC):
    @abstractmethod
    def save_feeling(self, path: str, content: str) -> bool:
        pass