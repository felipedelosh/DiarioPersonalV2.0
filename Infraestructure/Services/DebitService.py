"""
FelipedelosH
2025
"""
from Application.Services.IDebitServive import IDebitService
from Application.Repositories.IDebitRepository import IDebitRepository

class DebitService(IDebitService):
    def __init__(self, debit_repository: IDebitRepository):
        self.debit_repository = debit_repository

    def save_debit_report(self, path: str, content: str) -> bool:
        return self.debit_repository.save_debit_report(path, content)
