"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IDreamService(ABC):
    @abstractmethod
    def save_dream(self, path: str, content: str) -> bool:
        pass

    @abstractmethod
    def load_dream(self, path: str, keyword: str) -> Response:
        pass
