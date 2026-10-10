"""
FelipedelosH
2026
"""
# Application\UseCases\IGetAllYearsOfDrugsUsage.py
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGetAllYearsOfDrugsUsage(ABC):
    @abstractmethod
    def execute(self, path: str) -> Response:
        """
        path: path of drugs data folder
        Return all years [YYYY, ..., YYYY] of drugs usages in order
        """
        pass
