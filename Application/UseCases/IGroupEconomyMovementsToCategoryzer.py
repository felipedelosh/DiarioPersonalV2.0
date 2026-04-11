"""
FelipedelosH
2026

Gruoup Economy Data 
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGroupEconomyMovementsToCategoryzer(ABC):
    @abstractmethod
    def execute(self, base_path: str) -> Response:
        pass
