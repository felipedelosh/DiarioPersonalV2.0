"""
FelipedelosH
2025

Dependency Injector
"""

#Repositories
from Infraestructure.Repositories.FileDiaryRepository import FileDiaryRepository
from Infraestructure.Repositories.FileUsageRepository import FileUsageRepository
from Infraestructure.Repositories.FeelingRepository import FeelingRepository
#Services
from Infraestructure.Services.DiaryService import DiaryService
from Infraestructure.Services.UsageService import UsageService
from Infraestructure.Services.FeelingService import FeelingService
#Use Cases
from Infraestructure.UseCases.SaveDiaryPage import SaveDiaryPage
from Infraestructure.UseCases.loadDiaryPage import LoadDiaryPage
from Infraestructure.UseCases.SaveFeeling import SaveFeeling
# Utils
from Infraestructure.config.ConfigManager import ConfigManager
from Infraestructure.config.LanguageManager import LanguageManager
from CORE.UTILS.TimeUtils import TimeUtils
from CORE.UTILS.EnigmaByLoko import Enigma
from CORE.UTILS.StringProcesor import StringProcesor


class DependencyInjector:
    @staticmethod
    def build_dependencies():
        # Config
        configManager = ConfigManager()
        languageManager = LanguageManager("ASSETS/LAN", "ES")

        # REPOSITORIES
        diary_repo = FileDiaryRepository()
        usage_repo = FileUsageRepository()
        feeling_repo = FeelingRepository()
        # END REPOSITORIES

        # SERVICES
        diary_service = DiaryService(diary_repo)
        usage_servide = UsageService(usage_repo)
        feeling_service = FeelingService(feeling_repo)
        # END SERVICES

        # USECASES
        diary_use_case_save_page = SaveDiaryPage(diary_service)
        diary_use_case_load_page = LoadDiaryPage(diary_service)
        feeling_use_case_save = SaveFeeling(feeling_service)
        # END USECASES
        
        return {
            "usage_service": usage_servide,
            "diary_use_case_save_page": diary_use_case_save_page,
            "diary_use_case_load_page": diary_use_case_load_page,
            "feeling_use_case_save": feeling_use_case_save,
            "config": configManager,
            "lang": languageManager
            #...
        }


    @staticmethod
    def build_utils():
        time_util = TimeUtils()
        enigma = Enigma()
        string_procesor = StringProcesor()

        return {
            "time_util": time_util,
            "enigma": enigma,
            "string_procesor": string_procesor
        }
