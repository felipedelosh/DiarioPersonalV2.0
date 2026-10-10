"""
FelipedelosH
2026

This is the main contract to DRAW info of FEELINGS in BAR Graph
"""
# Application\Services\IGraphFeelsRenderer.py
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGraphFeelsRenderer(ABC):
    @abstractmethod
    def render(self, canvas, data: Response, options):
        pass
