"""
FelipedelosH
2025
"""
from Application.Services.IUsageService import IUsageService
from Application.Repositories.IUsageRepository import IUsageRepository

class UsageService(IUsageService):
    def __init__(self, usage_repo: IUsageRepository):
        self.usage_repo = usage_repo

    def save_usage(self, path: str, content: str) -> bool:
        return self.usage_repo.save_usage(path, content)