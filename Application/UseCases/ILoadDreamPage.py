"""
FelipedelosH
2025
"""
# Application\UseCases\ILoadDreamPage.py
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class ILoadDreamPage(ABC):
    @abstractmethod
    def execute(self,  path: str, keyword: str) -> Response:
        pass
