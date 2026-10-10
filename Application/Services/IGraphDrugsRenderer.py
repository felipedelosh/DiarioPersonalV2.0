"""
FelipedelosH
2026

This is the main contract to DRAW info of DRUGS in BAR Graph
"""
# Application\Services\IGraphDrugsRenderer.py
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IGraphDrugsRenderer(ABC):
    @abstractmethod
    def render(self, canvas, data: Response, options):
        pass
