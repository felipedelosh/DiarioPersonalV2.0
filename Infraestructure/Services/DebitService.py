"""
FelipedelosH
2025
"""
from Application.Services.IDebitServive import IDebitService
from Application.Repositories.IDebitRepository import IDebitRepository
from Domain.Entities.Response import Response

class DebitService(IDebitService):
    def __init__(self, debit_repository: IDebitRepository):
        self.debit_repository = debit_repository

    def save_debit_report(self, path: str, content: str) -> bool:
        return self.debit_repository.save_debit_report(path, content)

    def get_all_debit_path_report_by_year(self, path: str, YYYY: str) -> Response:
        return self.debit_repository.get_all_debit_path_report_by_year(path, YYYY)
