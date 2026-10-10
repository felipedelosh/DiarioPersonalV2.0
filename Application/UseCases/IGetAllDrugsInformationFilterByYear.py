"""
FelipedelosH
2026
"""
# Application\UseCases\IGetAllDrugsInformationFilterByYear.py
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGetAllDrugsInformationFilterByYear(ABC):
    @abstractmethod
    def execute(self, base_path: str, yyyy: str) -> Response:
        """
        base_path: MAIN folder of Drugs Data
        Returns a all data contains in DRUGS by YYYY
        """
        pass
