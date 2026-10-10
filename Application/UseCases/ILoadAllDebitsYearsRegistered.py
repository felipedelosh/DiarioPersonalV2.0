"""
FelipedelosH
2025
"""
# Application\UseCases\ILoadAllDebitsYearsRegistered.py
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class ILoadAllDebitsYearsRegistered(ABC):
    @abstractmethod
    def execute(self,  path: str) -> Response:
        pass
