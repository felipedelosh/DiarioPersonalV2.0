"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGetEconoyTAccountReport(ABC):
    @abstractmethod
    def execute(self, path: str) -> Response:
        pass
