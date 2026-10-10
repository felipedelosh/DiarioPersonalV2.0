"""
FelipedelosH
2026
"""
# Application\Services\IBackupService.py
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IBackupService(ABC):
    @abstractmethod
    def save(self, path: str, content: str) -> bool:
        pass
