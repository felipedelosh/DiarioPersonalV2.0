"""
FelipedelosH
2025
"""
from Application.UseCases.ILoadDreamPage import ILoadDreamPage
from Application.Services.IDreamService import IDreamService
from Domain.Entities.Response import Response

class LoadDreamPage(ILoadDreamPage):
    def __init__(self, dream_service: IDreamService):
        self.dream_service = dream_service

    def execute(self, path: str, content: str) -> Response:
        return self.dream_service.load_dream(path, content)
