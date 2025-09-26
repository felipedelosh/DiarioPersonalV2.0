"""
FelipedelosH
2025

PersonalDiaryV2.0
"""
from CORE.MainController import MainController
from CORE.DependencyInjector import DependencyInjector

controller = MainController(DependencyInjector.build_dependencies(), DependencyInjector.build_utils())
reqSaveStatus = controller.save_diary_page("titulo", "Hoy avancé mucho en mi diario personal")
print(f"Status: {reqSaveStatus}")
