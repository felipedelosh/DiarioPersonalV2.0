"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class IUsageService(ABC):
    @abstractmethod
    def save_usage(self, path: str, data: str) -> bool:
        pass