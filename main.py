"""
FelipedelosH
2025

PersonalDiaryV2.0
"""
from CORE.MainController import MainController
from CORE.DependencyInjector import DependencyInjector

controller = MainController(DependencyInjector.build_dependencies(), DependencyInjector.build_utils())
controller.save_diary_page("DATA/DIARIO/2025/page1.txt", "Hoy avancé mucho en mi diario personal")
