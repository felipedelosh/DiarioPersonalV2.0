"""
FelipedelosH
2025

Dependency Injector
"""

#Repositories
from Infraestructure.Repositories.FileDiaryRepository import FileDiaryRepository
from Infraestructure.Repositories.FileUsageRepository import FileUsageRepository
#Services
from Infraestructure.Services.DiaryService import DiaryService
from Infraestructure.Services.UsageService import UsageService
#Use Cases
from Infraestructure.UseCases.SaveDiaryPage import SaveDiaryPage
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
        # END REPOSITORIES

        # SERVICES
        diary_service = DiaryService(diary_repo)
        usage_servide = UsageService(usage_repo)
        # END SERVICES

        # USECASES
        diary_use_case_save_page = SaveDiaryPage(diary_service)
        # END USECASES
        
        return {
            "usage_service": usage_servide,
            "diary_use_case_save_page": diary_use_case_save_page,
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
