"""
FelipdelosH
2026

Implementation of Graphier
"""
from Application.Services.IGraphRenderer import IGraphRenderer
from Domain.Entities.Response import Response

class GraphRenderer(IGraphRenderer):
    def __init__(self):
        pass

    def render(self, canvas, data: Response, graphicsType: str, options):
        print("Graphier By LOKO")
