"""
FelipedelosH
2025
"""
from Application.UseCases.IGetAllFoldersInPath import IGetAllFoldersInPath
from Application.Services.IFolderService import IFolderService
from Domain.Entities.Response import Response

class GetAllFoldersInPath(IGetAllFoldersInPath):
    def __init__(self, folder_service: IFolderService):
        self.folder_service = folder_service

    def execute(self, path) -> Response:
        return self.folder_service.get_all_folders_in_path(path)
