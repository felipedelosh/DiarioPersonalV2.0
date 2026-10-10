"""
FelipedelosH
2025
"""
# Application\UseCases\IGetEconoyTAccountReport.py
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGetEconoyTAccountReport(ABC):
    @abstractmethod
    def execute(self, path: str) -> Response:
        pass
