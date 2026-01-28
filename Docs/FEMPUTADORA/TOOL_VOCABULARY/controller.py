"""
FelipedelosH
2026
"""
import json
import os
from os import scandir

class Controller:
    def __init__(self) -> None:
        self.path = os.getcwd()
        self.template = ""
        self.config = self.loadConfig()

    def loadConfig(self):
        try:
            config = ""
            with open(f"{self.path}/config.json", "r", encoding="UTF-8") as f:
                config = json.load(f)

            return config
        except:
            return None


    def getTextInFile(self, path):
        info = None
        try:
            f = open(path, 'r', encoding="utf-8")
            return f.read()
        except:
            return info
        
    def getAllFilesInFolderFilteredByExt(self, ext, path):
        """
        Return all files names of data folder
        """
        try:
            path = os.getcwd() + f"/{path}"

            filesNames = []
            for i in scandir(path):
                if i.is_file():
                    if ext in i.name:
                        filesNames.append(i.name)
            return filesNames
        except:
            return None
