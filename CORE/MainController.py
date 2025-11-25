"""
FelipedelosH
2025

Main Controller
"""
import sys
import os
from CORE.FolderController import FolderController
from CORE.PathController import PathController

class MainController:
    def __init__(self, dependencies: dict, utils: dict):
        self.path = str(os.path.abspath(os.path.dirname(sys.argv[0])))
        # Inyections
        self.dependencies = dependencies
        self.utils = utils
        # Controllers
        self.folderController = FolderController(self.path, self.utils["time_util"])
        self.pathController = PathController(self.path, self.utils["time_util"])
