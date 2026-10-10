"""
FelipedelosH
2026
"""
# Application\UseCases\IGetAllYearsOfFeelsUsage.py
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGetAllYearsOfFeelsUsage(ABC):
    @abstractmethod
    def execute(self, path: str) -> Response:
        """
        path: path of feelings data folder
        Return all years [YYYY, ..., YYYY] of feelings usages in order
        """
        pass
