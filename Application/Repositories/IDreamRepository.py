"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class IDreamRepository(ABC):
    @abstractmethod
    def save_dream_page(self, path: str, content: str) -> bool:
        pass
