"""
FelipedelosH
2026


Generates a Response with all INFORMATION
Generate a file DATA/TEMP/all.txt 
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGetAllDiaryInformationWithTempFile(ABC):
    @abstractmethod
    def execute(self, pathArr: list) -> Response:
        pass
