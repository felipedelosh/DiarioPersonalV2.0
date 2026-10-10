"""
FelipedelosH
2026
"""
from Application.UseCases.IGetAllDrugsInformationFilterByYear import IGetAllDrugsInformationFilterByYear
from Application.Services.IFolderService import IFolderService
from Application.Services.IDrugService import IDrugService
from Domain.Entities.Response import Response

class GetAllDrugsInformationFilterByYear(IGetAllDrugsInformationFilterByYear):
    def __init__(self, folder_service: IFolderService, drug_service: IDrugService):
        self.folder_service = folder_service
        self.drug_service = drug_service

    def execute(self, base_path: str, yyyy: str) -> Response:
        try:
            _data = self.folder_service.get_all_files_in_path_by_ext(f"{base_path}{yyyy}", "txt")

            if not _data["success"] or _data["qty"] <= 0:
                return Response.response(False, {}, -1)

            _qty = 0
            _final_data = {}
            for i in _data["data"]:
                _drug_file_path = f"{base_path}{yyyy}/{i}"
                _drug_info = self.drug_service.get_drug_info(_drug_file_path)
                _final_data[_drug_file_path] = _drug_info
                _qty = _qty + 1

            return Response.response(True, _final_data, _qty)
        except:
            return Response.response(False, {}, -1)
