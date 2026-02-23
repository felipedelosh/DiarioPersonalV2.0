"""
FelipedelosH
2025
"""
from abc import ABC, abstractmethod
from Domain.Entities.Response import Response

class IFolderService(ABC):
    @abstractmethod
    def get_all_folders_in_path(self, path: str) -> Response:
        pass

    @abstractmethod
    def get_all_files_in_path_by_ext(self, path: str, ext: str) -> Response:
        pass
