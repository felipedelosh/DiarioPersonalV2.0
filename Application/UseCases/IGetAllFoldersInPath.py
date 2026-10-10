"""
FelipedelosH
2025
"""
# Application\UseCases\IGetAllFoldersInPath.py
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGetAllFoldersInPath(ABC):
    @abstractmethod
    def execute(self, path: str) -> Response:
        pass
