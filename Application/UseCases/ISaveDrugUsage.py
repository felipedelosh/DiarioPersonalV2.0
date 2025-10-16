"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class ISaveDrugUsage(ABC):
    @abstractmethod
    def execute(self, path: str, content: str) -> bool:
        pass
