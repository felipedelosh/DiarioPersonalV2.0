"""
FelipedelosH
2026
"""
# Application\UseCases\IChatWithFemputadora.py
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IChatWithFemputadora(ABC):
    @abstractmethod
    def execute(self, txt: str) -> Response:
        pass
