"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class IDiaryService(ABC):
    @abstractmethod
    def save_page(self, path: str, content: str) -> bool:
        pass