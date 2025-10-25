"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class IEconomyService(ABC):
    @abstractmethod
    def save_economy_taccount_report(self, path: str, content: str) -> bool:
        pass
