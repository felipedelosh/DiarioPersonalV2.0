"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IDiaryRepository(ABC):
    @abstractmethod
    def save_diary_page(self, path: str, content: str) -> bool:
        pass

    @abstractmethod
    def load_diary_page(self, path: str, keyword: str) -> Response:
        pass
