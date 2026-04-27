"""
FelipedelosH
2026
"""
from abc import ABC, abstractmethod

class ISaveScheduleDay24(ABC):
    @abstractmethod
    def execute(self, base_path: str, specify_path, content: str) -> bool:
        pass
