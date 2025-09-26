"""
FelipedelosH
2025

Dependency Injector
"""
from CORE.MainController import MainController
from Infraestructure.Repositories.FileDiaryRepository import FileDiaryRepository

class DependencyInjector:
    @staticmethod
    def build_main_controller():

        # REPOSITORIES
        diary_repo = FileDiaryRepository()
        controller = MainController(diary_repo)
        # END REPOSITORIES


        return controller
