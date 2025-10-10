"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class ILoadDreamPage(ABC):
    @abstractmethod
    def execute(self,  path: str, keyword: str) -> Response:
        pass
