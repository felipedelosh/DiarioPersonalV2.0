"""
FelipedelosH
2025
"""
from Application.UseCases.ISaveDrugUsage import ISaveDrugUsage
from Application.Services.IDrugService import IDrugService

class SaveDrugUsage(ISaveDrugUsage):
    def __init__(self, service: IDrugService):
        self.drug_service = service

    def execute(self, path: str, content: str) -> bool:
        return self.drug_service.save_drug_usage(path, content)
