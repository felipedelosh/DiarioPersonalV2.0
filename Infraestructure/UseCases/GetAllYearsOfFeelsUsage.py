"""
FelipedelosH
2026
"""
# Infraestructure\UseCases\GetAllYearsOfFeelsUsage.py
from Application.UseCases.IGetAllYearsOfFeelsUsage import IGetAllYearsOfFeelsUsage
from Application.Services.IFolderService import IFolderService
from Domain.Entities.Response import Response

class GetAllYearsOfFeelsUsage(IGetAllYearsOfFeelsUsage):
    def __init__(self, folder_service: IFolderService):
        self.folder_service = folder_service

    def execute(self, path: str) -> Response:
        try:
            _YYYY = []
            _data = self.folder_service.get_all_folders_in_path(path)

            if not _data["success"] or _data["qty"] <= 0:
                return Response.response(False, {}, -1)

            for i in _data["data"]:
                _YYYY.append(_data["data"][i])

            if not _YYYY:
                return Response.response(False, {}, -1)

            _YYYY.sort()
            _final_data = {}
            _counter = 0
            for i in _YYYY:
                _final_data[_counter] = i
                _counter = _counter + 1

            return Response.response(True, _final_data, _counter)
        except:
            return Response.response(False, {}, -1)
