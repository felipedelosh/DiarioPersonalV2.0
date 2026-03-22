"""
FelipedelosH
2025
"""
from Application.Services.IBackupService import IBackupService
from Application.Repositories.IBackuprepository import IBackupRepository
from Domain.Entities.Response import Response

class BackupService(IBackupService):
    def __init__(self, backup_repo: IBackupRepository):
        self.backup_repo = backup_repo

    def save(self, path: str, content: str) -> bool:
        return self.backup_repo.save(path, content)