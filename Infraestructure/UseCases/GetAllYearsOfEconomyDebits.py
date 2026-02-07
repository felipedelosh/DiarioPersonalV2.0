"""
FelipedelosH
2026
"""
from Application.UseCases.IGetAllYearsOfEconomyDebits import IGetAllYearsOfEconomyDebits
from Application.Services.IFolderService import IFolderService
from Domain.Entities.Response import Response

class GetAllYearsOfEconomyDebits(IGetAllYearsOfEconomyDebits):
    def __init__(self, service_folder: IFolderService):
        self.service_folder = service_folder

    def execute(self, base_path) -> Response:
        _data = self.service_folder.get_all_folders_in_path(base_path)

        if not _data["success"]:
            return Response.response(False, [], 0)
        
        _YYYY = [valor for _, valor in _data["data"].items()]
        return Response.response(True, _YYYY, len(_YYYY))
