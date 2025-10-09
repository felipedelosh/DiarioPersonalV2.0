"""
FelipedelosH
2025
"""
from Application.Services.IDreamService import IDreamService
from Application.Repositories.IDreamRepository import IDreamRepository

class DiaryService(IDreamService):
    def __init__(self, dream_repository: IDreamRepository):
        self.dream_repository = dream_repository

    def save_dream(self, path: str, content: str) -> bool:
        return self.dream_repository.save_dream_page(path, content)
