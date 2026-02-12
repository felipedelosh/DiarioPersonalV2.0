"""
FelipedelosH
2026

RULES -> ALL SAVE IN UPPER CASE
"""
import uuid
import json
import os
from os import scandir
from src.models.SemanticDimension import SemanticDimensión

class Controller:
    def __init__(self) -> None:
        self.path = os.getcwd()
        self.template = ""
        self.config = self.loadConfig()

        # VARS
        self.semanticDimensionsArr = []

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
        
    def setSemanticDimsension(self, title, contexIterators, textSDimenDescript):
        _id = str(uuid.uuid4())
        iterators_arr = [x.strip() for x in contexIterators.split(",") if x.strip()]

        self.semanticDimensionsArr.append(
            SemanticDimensión(
                _id,
                title,
                iterators_arr,
                textSDimenDescript
            )
        )

    def saveWork(self):
        print(f"Vamos a guardar: {self.semanticDimensionsArr}")
