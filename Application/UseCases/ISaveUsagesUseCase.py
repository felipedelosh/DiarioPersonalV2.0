"""
FelipedelosH
2025
"""
# Application\UseCases\ISaveUsagesUseCase.py
from abc import ABC, abstractmethod

class ISaveUsage(ABC):
    @abstractmethod
    def execute(self, path: str, YYYY: str, typeUsage: str, timeStamp: str) -> bool:
        pass
