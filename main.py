"""
FelipedelosH
2025

PersonalDiaryV2.0
"""
from CORE.DependencyInjector import DependencyInjector

controller = DependencyInjector.build_main_controller()
controller.save_diary_page("DATA/DIARIO/2025/page1.txt", "Hoy avancé mucho en mi diario personal")
