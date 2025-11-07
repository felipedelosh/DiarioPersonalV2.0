"""
FelipedelosH
2025
"""
import uuid
from Application.Services.IDebitServive import IDebitService
from Application.UseCases.ISaveDebitReport import ISaveDebitReport

class SaveDebitReport(ISaveDebitReport):
    def __init__(self, debit_service: IDebitService):
        self.debit_service = debit_service

    def execute(self, path, content):
        UUID = str(uuid.uuid4())
        content = f"{UUID}|{content}"
        return self.debit_service.save_debit_report(path, content)
