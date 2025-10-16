"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod

class IDrugRepository(ABC):
    @abstractmethod
    def save_drug_usage(self, path: str, content: str) -> bool:
        pass
