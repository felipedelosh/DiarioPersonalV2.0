"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IEconomyService(ABC):
    @abstractmethod
    def save_economy_taccount_report(self, path: str, content: str) -> bool:
        pass

    @abstractmethod
    def update_economy_taccount_report(self, path: str, content: str) -> bool:
        pass

    @abstractmethod
    def get_economy_taccount_report(self, path: str) -> Response:
        pass
