"""
FelipedelosH
2026
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGetPaginatedFromData(ABC):
    @abstractmethod
    def execute(self, response: dict, page: int, page_size: int) -> Response:
        pass
