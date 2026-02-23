"""
FelipedelosH
2026

This is the main contract to DRAW info

Example: Draw BarChart... 
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGraphRenderer(ABC):
    @abstractmethod
    def render(self, canvas, data: Response, graphicsType: str, options):
        pass
