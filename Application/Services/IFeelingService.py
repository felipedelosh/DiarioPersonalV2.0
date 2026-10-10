"""
FelipedelosH
2025
"""
# Application\Services\IFeelingService.py
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IFeelingService(ABC):
    @abstractmethod
    def save_feeling(self, path: str, content: str) -> bool:
        pass

    @abstractmethod
    def get_feel_info(self, path: str) -> Response:
        pass
