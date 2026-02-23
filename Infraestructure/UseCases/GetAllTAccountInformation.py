"""
FelipedelosH
2026
"""
from Application.UseCases.IGetAllTAccountInformation import IGetAllTAccountInformation
from Application.Services.IFolderService import IFolderService
from Application.Services.IEconomyService import IEconomyService
from Domain.Entities.Response import Response

class GetAllTAccountInformation(IGetAllTAccountInformation):
    def __init__(self, folder_service: IFolderService, economy_service: IEconomyService):
        self.folder_service = folder_service
        self.economy_service = economy_service

    def execute(self, base_path: str) -> Response:
        try:
            _data_by_YYYY = self.folder_service.get_all_folders_in_path(base_path)
            if not _data_by_YYYY["success"]:
                return Response.response(False, {}, 0)

            _counter_final_data = 0
            _final_data = {}
            for i in _data_by_YYYY["data"]:
                _YYYY = _data_by_YYYY["data"][i]
                _data_files_in_yyyy_folder = self.folder_service.get_all_files_in_path_by_ext(f"{base_path}{_YYYY}", ".csv")
                if not _data_files_in_yyyy_folder["success"] and _data_files_in_yyyy_folder["success"] == 0:
                    continue

                for itterData in _data_files_in_yyyy_folder["data"]:
                    _file_path = f"{base_path}{_YYYY}/{itterData}"

                    _taacount_data = self.economy_service.get_economy_taccount_report(_file_path)

                    if not _taacount_data["success"]:
                        continue
                        
                    data_dict = _taacount_data.get("data", {})
                    k, v = next(iter(data_dict.items()))

                    _final_data[k] = v
                    
                    _counter_final_data = _counter_final_data + 1

            return Response.response(True, _final_data, _counter_final_data)
        except:
            return Response.response(False, {}, 0)
