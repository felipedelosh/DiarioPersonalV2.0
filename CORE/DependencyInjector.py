"""
FelipedelosH
2025

Dependency Injector
"""

#Repositories
from Infraestructure.Repositories.FileDiaryRepository import FileDiaryRepository
from Infraestructure.Repositories.FileUsageRepository import FileUsageRepository
from Infraestructure.Repositories.FeelingRepository import FeelingRepository
from Infraestructure.Repositories.DreamRepository import FileDreamRepository
from Infraestructure.Repositories.DrugRepository import DrugRepository
from Infraestructure.Repositories.EconomyRepository import FileEconomyRepository
from Infraestructure.Repositories.FileDebitRepository import FileDebitRepository
from Infraestructure.Repositories.ScheduleRepository import ScheduleRepository
#Services
from Infraestructure.Services.DiaryService import DiaryService
from Infraestructure.Services.UsageService import UsageService
from Infraestructure.Services.FeelingService import FeelingService
from Infraestructure.Services.DreamService import DreamService
from Infraestructure.Services.DrugService import DrugService
from Infraestructure.Services.EconomyService import EconomyService
from Infraestructure.Services.DebitService import DebitService
from Infraestructure.Services.FolderService import FolderService
from Infraestructure.Services.ScheduleService import ScheduleService
#Use Cases
from Infraestructure.UseCases.SaveDiaryPage import SaveDiaryPage
from Infraestructure.UseCases.loadDiaryPage import LoadDiaryPage
from Infraestructure.UseCases.SaveFeeling import SaveFeeling
from Infraestructure.UseCases.SaveDreamPage import SaveDreamPage
from Infraestructure.UseCases.LoadDreamPage import LoadDreamPage
from Infraestructure.UseCases.SaveDrugUsage import SaveDrugUsage
from Infraestructure.UseCases.SaveEconomyTAccountReport import SaveEconomyTAccountReport
from Infraestructure.UseCases.SaveDebitReport import SaveDebitReport
from Infraestructure.UseCases.loadAllDebitsPeerYear import LoadAllDebitsPeerYear
from Infraestructure.UseCases.PayDebit import PayDebit
from Infraestructure.UseCases.GetAllFoldersInPath import GetAllFoldersInPath
from Infraestructure.UseCases.LoadAllDebitsYearsRegistered import LoadAllDebitsYearsRegistered
from Infraestructure.UseCases.GetEconoyTAccountReport import GetEconoyTAccountReport
from Infraestructure.UseCases.GetAllInformationEconomy import GetAllInformationEconomy
from Infraestructure.UseCases.SaveSchedule24HReport import SaveSchedule24HReport
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
        dream_repo = FileDreamRepository()
        drug_repo = DrugRepository()
        economy_repo = FileEconomyRepository()
        debit_repo = FileDebitRepository()
        schedule_repo = ScheduleRepository()
        # END REPOSITORIES

        # SERVICES
        diary_service = DiaryService(diary_repo)
        usage_servide = UsageService(usage_repo)
        feeling_service = FeelingService(feeling_repo)
        dream_service = DreamService(dream_repo)
        drug_service = DrugService(drug_repo)
        economy_service = EconomyService(economy_repo)
        debit_service = DebitService(debit_repo)
        folder_service = FolderService()
        schedule_service = ScheduleService(schedule_repo)
        # END SERVICES

        # USECASES
        folders_use_case_get_all = GetAllFoldersInPath(folder_service)
        diary_use_case_save_page = SaveDiaryPage(diary_service)
        diary_use_case_load_page = LoadDiaryPage(diary_service)
        feeling_use_case_save = SaveFeeling(feeling_service)
        dream_use_case_save_dream = SaveDreamPage(dream_service)
        dream_use_case_load_dream = LoadDreamPage(dream_service)
        drug_use_case_save_usage = SaveDrugUsage(drug_service)
        economy_use_case_save_taccount = SaveEconomyTAccountReport(economy_service)
        economy_use_case_get_taccount = GetEconoyTAccountReport(economy_service)
        economy_use_case_get_all_info = GetAllInformationEconomy(folder_service, debit_service)
        debit_use_case_save_report = SaveDebitReport(debit_service)
        debit_use_case_load_all_debits_peer_year = LoadAllDebitsPeerYear(debit_service)
        debit_use_case_pay_debit = PayDebit(debit_service)
        debit_use_case_get_all_debits_registered = LoadAllDebitsYearsRegistered(folders_use_case_get_all, debit_use_case_load_all_debits_peer_year)
        schedule_use_case_save_24h_report = SaveSchedule24HReport(schedule_service)
        # END USECASES
        
        return {
            "usage_service": usage_servide,
            "folders_use_case_get_all": folders_use_case_get_all,
            "diary_use_case_save_page": diary_use_case_save_page,
            "diary_use_case_load_page": diary_use_case_load_page,
            "dream_use_case_save_dream": dream_use_case_save_dream,
            "dream_use_case_load_dream": dream_use_case_load_dream,
            "feeling_use_case_save": feeling_use_case_save,
            "drug_use_case_save_usage": drug_use_case_save_usage,
            "economy_use_case_save_taccount": economy_use_case_save_taccount,
            "economy_use_case_get_taccount": economy_use_case_get_taccount,
            "economy_use_case_get_all_info": economy_use_case_get_all_info,
            "debit_use_case_save_report": debit_use_case_save_report,
            "debit_use_case_load_all_debits_peer_year": debit_use_case_load_all_debits_peer_year,
            "debit_use_case_pay_debit": debit_use_case_pay_debit,
            "debit_use_case_get_all_debits_registered": debit_use_case_get_all_debits_registered,
            "schedule_use_case_save_24h_report": schedule_use_case_save_24h_report,
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
