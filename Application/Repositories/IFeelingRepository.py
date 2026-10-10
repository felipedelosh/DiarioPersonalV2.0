"""
FelipedelosH
2025
"""
# Application\Repositories\IFeelingRepository.py
from abc import ABC, abstractmethod

class IFeelingRepository(ABC):
    @abstractmethod
    def save_feeling(self, path: str, data: str) -> bool:
        pass
