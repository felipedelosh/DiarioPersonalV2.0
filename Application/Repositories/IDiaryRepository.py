"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class IDiaryRepository(ABC):
    @abstractmethod
    def save_diary_page(self, path: str, content: str) -> None:
        pass
