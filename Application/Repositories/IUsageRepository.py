"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class IUsageRepository(ABC):
    @abstractmethod
    def save_usage(self, path: str, data: str) -> bool:
        pass
