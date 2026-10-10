"""
FelipedelosH
2025
"""
# Application\UseCases\ISaveDreamPage.py
from abc import ABC, abstractmethod

class ISaveDreamPage(ABC):
    @abstractmethod
    def execute(self, path: str, content: str) -> bool:
        pass