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
    def execute(self, pathDic: dict, path_backup_file: str, backup_file_header_template: str) -> Response:
        pass
