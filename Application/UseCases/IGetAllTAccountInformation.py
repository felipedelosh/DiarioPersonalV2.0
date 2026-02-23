"""
FelipedelosH
2026

Returns all TACCOUNTS information in RESPONSE
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGetAllTAccountInformation(ABC):
    @abstractmethod
    def execute(self, base_path: str) -> Response:
        """
        {path_file: 'INFO'}
        """
        pass
