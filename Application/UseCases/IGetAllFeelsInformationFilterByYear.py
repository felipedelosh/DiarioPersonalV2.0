"""
FelipedelosH
2026
"""
# Application\UseCases\GetAllFeelsInformationFilterByYear.py
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGetAllFeelsInformationFilterByYear(ABC):
    @abstractmethod
    def execute(self, base_path: str, yyyy: str) -> Response:
        """
        base_path: MAIN folder of Feelings Data
        Returns all data contained in FEELINGS by YYYY
        """
        pass
