"""
FelipedelosH
2025
"""
# Application\UseCases\ISaveDiaryPage.py
from abc import ABC, abstractmethod

class ISaveDiaryPage(ABC):
    @abstractmethod
    def execute(self, path: str, content: str) -> bool:
        pass
