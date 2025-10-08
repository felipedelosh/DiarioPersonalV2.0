"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IDiaryService(ABC):
    @abstractmethod
    def save_page(self, path: str, content: str) -> bool:
        pass

    @abstractmethod
    def load_page(self, path: str, keyword: str) -> Response:
        pass
