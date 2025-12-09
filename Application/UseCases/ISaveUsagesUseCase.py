"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class ISaveUsage(ABC):
    @abstractmethod
    def execute(self, path: str, timeStamp: str) -> bool:
        pass
