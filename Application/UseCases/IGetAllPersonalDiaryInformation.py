"""
FelipedelosH
2026

Get ALL write in personal diary in Response:
data = {"key": "text"}
"""
# Application\UseCases\IGetAllPersonalDiaryInformation.py
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGetAllPersonalDiaryInformation(ABC):
    @abstractmethod
    def execute(self, base_path: str) -> Response:
        pass
