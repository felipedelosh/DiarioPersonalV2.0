"""
FelipedelosH
2025

Return all folders in a given path order by YYYY
"""
from Application.UseCases.IGetAllFoldersInPath import IGetAllFoldersInPath
from Application.Services.IFolderService import IFolderService
from Domain.Entities.Response import Response

class GetAllFoldersInPath(IGetAllFoldersInPath):
    def __init__(self, folder_service: IFolderService):
        self.folder_service = folder_service

    def execute(self, path) -> Response:
        _data = self.folder_service.get_all_folders_in_path(path)

        if not _data["success"] or _data["qty"] == 0:
            return Response.response(False, {}, 0)

        years = list(_data["data"].values())

        years = sorted(years, key=int)

        _data["data"] = {
            index: year for index, year in enumerate(years)
        }

        return _data
