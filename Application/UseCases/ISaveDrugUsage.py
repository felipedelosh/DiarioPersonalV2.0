"""
FelipedelosH
2025
"""
# Application\UseCases\ISaveDrugUsage.py
from abc import ABC, abstractmethod

class ISaveDrugUsage(ABC):
    @abstractmethod
    def execute(self, path: str, content: str) -> bool:
        pass
