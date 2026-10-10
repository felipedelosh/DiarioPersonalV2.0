"""
FelipedelosH
2025
"""
# Application\Services\IDrugService.py
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IDrugService(ABC):
    @abstractmethod
    def save_drug_usage(self, path: str, content: str) -> bool:
        pass

    @abstractmethod
    def get_drug_info(self, path: str) -> Response:
        pass
