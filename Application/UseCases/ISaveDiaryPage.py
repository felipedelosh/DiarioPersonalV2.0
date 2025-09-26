"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class ISaveDiaryPage(ABC):
    @abstractmethod
    def save_page(self, path: str, content: str) -> None:
        pass
