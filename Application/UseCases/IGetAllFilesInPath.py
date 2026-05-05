"""
FelipedelosH
2026
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGetAllFilesInPath(ABC):
    @abstractmethod
    def execute(self, path: str, ext: str) -> Response:
        pass
