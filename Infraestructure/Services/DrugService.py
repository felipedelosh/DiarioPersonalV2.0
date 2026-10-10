"""
FelipedelosH
2025
"""
from Application.Services.IDrugService import IDrugService
from Application.Repositories.IDrugRepository import IDrugRepository
from Domain.Entities.Response import Response

class DrugService(IDrugService):
    def __init__(self, drug_repo: IDrugRepository):
        self.drug_repo = drug_repo

    def save_drug_usage(self, path: str, content: str) -> bool:
        return self.drug_repo.save_drug_usage(path, content)

    def get_drug_info(self, path: str) -> Response:
        return self.drug_repo.get_drug_info(path)
