"""
FelipedelosH
2026
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IBackupRepository(ABC):
    @abstractmethod
    def save(self, path: str, content: str) -> bool:
        pass
