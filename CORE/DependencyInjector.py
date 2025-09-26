"""
FelipedelosH
2025

Dependency Injector
"""
#Repositories
from Infraestructure.Repositories.FileDiaryRepository import FileDiaryRepository
#Services
from Infraestructure.Services.DiaryService import DiaryService

class DependencyInjector:
    @staticmethod
    def build_dependencies():

        # REPOSITORIES
        diary_repo = FileDiaryRepository()
        # END REPOSITORIES

        # SERVICES
        diary_service = DiaryService(diary_repo)
        # END SERVICES

        return {
            "diary_service": diary_service,
            #...
        }
