"""
FelipedelosH
2025
"""
# Application\Repositories\IFeelingRepository.py
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IFeelingRepository(ABC):
    @abstractmethod
    def save_feeling(self, path: str, data: str) -> bool:
        pass

    @abstractmethod
    def get_feel_info(self, path: str) -> Response:
        pass
