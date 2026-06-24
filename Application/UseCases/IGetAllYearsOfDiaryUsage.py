"""
FelipedelosH
2026
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGetAllYearsOfDiaryUsage(ABC):
    @abstractmethod
    def execute(self, path_dict: dict) -> Response:
        """
        path_arr: diary data paths
        Return all years [YYYY, ..., YYYY] of diary usages
        """
        pass
