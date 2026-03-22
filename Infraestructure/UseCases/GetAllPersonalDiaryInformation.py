"""
FelipedelosH
2026
"""
from Application.UseCases.IGetAllPersonalDiaryInformation import IGetAllPersonalDiaryInformation
from Application.Services.IFolderService import IFolderService
from Application.Services.IDiaryService import IDiaryService
from Domain.Entities.Response import Response

class GetAllPersonalDiaryInformation(IGetAllPersonalDiaryInformation):
    def __init__(self, folder_service: IFolderService, diary_service: IDiaryService):
        self.folder_service = folder_service
        self.diary_service = diary_service

    def execute(self, base_path: str) -> Response:
        try:
            _qty = 0

            _data_by_YYYY = self.folder_service.get_all_folders_in_path(base_path)
            if not _data_by_YYYY["success"]:
                return Response.response(False, {}, 0)
            
            _final_data = {}
            for i in _data_by_YYYY["data"]:
                _YYYY = _data_by_YYYY["data"][i]
                _data_files_in_yyyy_folder = self.folder_service.get_all_files_in_path_by_ext(f"{base_path}{_YYYY}", ".txt")
                if not _data_files_in_yyyy_folder["success"] and _data_files_in_yyyy_folder["success"] == 0:
                    continue

                for itterData in _data_files_in_yyyy_folder["data"]:
                    _file_path = f"{base_path}{_YYYY}"
                    _keyword = itterData
                    _diary_data = self.diary_service.load_page(_file_path, _keyword)

                    if _diary_data["success"] and _diary_data["qty"] > 0:
                        _final_data[_diary_data["data"]["title"]] = _diary_data["data"]["content"]
                        _qty = _qty + 1

            return Response.response(True, _final_data, _qty)
        except:
            return Response.response(False, {}, -1)
