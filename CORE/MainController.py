"""
FelipedelosH
2025

Main Controller
"""
from Application.Repositories.IDiaryRepository import IDiaryRepository

class MainController:
    def __init__(self, diary_repository: IDiaryRepository):
        # Inyectamos el repositorio (cumple con el contrato)
        self.diary_repository = diary_repository

    def save_diary_page(self, path: str, content: str):
        # Delegamos al repositorio inyectado
        self.diary_repository.save_diary_page(path, content)
