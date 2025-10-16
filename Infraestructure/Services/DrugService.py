"""
FelipedelosH
2025
"""
from Application.Services.IDrugService import IDrugService
from Application.Repositories.IDrugRepository import IDrugRepository

class DrugService(IDrugService):
    def __init__(self, drug_repo: IDrugRepository):
        self.drug_repo = drug_repo

    def save_drug_usage(self, path: str, content: str) -> bool:
        return self.drug_repo.save_drug_usage(path, content)
