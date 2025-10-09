"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class IDreamService(ABC):
    @abstractmethod
    def save_dream(self, path: str, content: str) -> bool:
        pass
