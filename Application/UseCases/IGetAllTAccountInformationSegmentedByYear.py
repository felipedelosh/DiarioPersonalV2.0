"""
FelipedelosH
2026

Returns all TACCOUNTS segmente by years information in RESPONSE
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGetAllTAccountInformationSegmentedByYear(ABC):
    @abstractmethod
    def execute(self, base_path: str) -> Response:
        """
            {YYYY:
                {'FILE_PATH': 'DATA'}
            }
        """
        pass
