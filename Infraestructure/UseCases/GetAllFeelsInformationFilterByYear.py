"""
FelipedelosH
2026
"""
# Infraestructure\UseCases\GetAllFeelsInformationFilterByYear.py
from Application.UseCases.IGetAllFeelsInformationFilterByYear import IGetAllFeelsInformationFilterByYear
from Application.Services.IFolderService import IFolderService
from Application.Services.IFeelingService import IFeelingService
from Domain.Entities.Response import Response

class GetAllFeelsInformationFilterByYear(IGetAllFeelsInformationFilterByYear):
    def __init__(self, folder_service: IFolderService, feeling_service: IFeelingService):
        self.folder_service = folder_service
        self.feeling_service = feeling_service

    def execute(self, base_path: str, yyyy: str) -> Response:
        try:
            _data = self.folder_service.get_all_files_in_path_by_ext(f"{base_path}{yyyy}", ".txt")

            if not _data["success"] or _data["qty"] <= 0:
                return Response.response(False, {}, -1)

            _qty = 0
            _final_data = {}
            for i in _data["data"]:
                _feel_file_path = f"{base_path}{yyyy}/{i}"
                _feel_info = self.feeling_service.get_feel_info(_feel_file_path)

                if not _feel_info["success"] or _feel_info["qty"] <= 0:
                    continue

                # Unwrap the inner Response -> get the plain sentiment string
                _inner_data = _feel_info["data"]
                for inner_path in _inner_data:
                    _final_data[_feel_file_path] = _inner_data[inner_path]

                _qty = _qty + 1

            return Response.response(True, _final_data, _qty)
        except:
            return Response.response(False, {}, -1)