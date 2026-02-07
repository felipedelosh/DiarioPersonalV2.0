"""
FelipedelosH
2026
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGetAllYearsOfEconomyDebits(ABC):
    @abstractmethod
    def execute(self,  base_path: str) -> Response:
        """
        Return all years [YYYY, ..., YYYY] of Debit Accounts
        """
        pass
