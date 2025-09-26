"""
FelipedelosH
2025

Dependency Injector
"""

#Repositories
from Infraestructure.Repositories.FileDiaryRepository import FileDiaryRepository
#Services
from Infraestructure.Services.DiaryService import DiaryService
#Use Cases
from Infraestructure.UseCases.SaveDiaryPage import SaveDiaryPage
# Utils
from CORE.UTILS.TimeUtils import TimeUtils


class DependencyInjector:
    @staticmethod
    def build_dependencies():

        # REPOSITORIES
        diary_repo = FileDiaryRepository()
        # END REPOSITORIES

        # SERVICES
        diary_service = DiaryService(diary_repo)
        # END SERVICES

        # USECASES
        diary_use_case = SaveDiaryPage(diary_service)
        # END USECASES

        return {
            "diary_use_case": diary_use_case,
            #...
        }


    @staticmethod
    def build_utils():
        time_util = TimeUtils()

        return {
            "time_util": time_util
        }
