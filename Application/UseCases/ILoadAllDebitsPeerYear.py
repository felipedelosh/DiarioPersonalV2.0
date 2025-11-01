"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class ILoadAllDebitsPeerYear(ABC):
    @abstractmethod
    def execute(self,  path: str, YYYY: str) -> Response:
        pass
