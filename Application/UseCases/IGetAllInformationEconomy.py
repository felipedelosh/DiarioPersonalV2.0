"""
FelipedelosH
2025
"""
# Application\UseCases\IGetAllInformationEconomy.py
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGetAllInformationEconomy(ABC):
    @abstractmethod
    def execute(self,  base_path: str, keyword: str, initDate: str, finalDate: str) -> Response:
        """
        Returns a Response with data of all economy movements the data is:
        DATE|CONCEPT|CASH|TYPE|STATUS
        """
        pass
