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
        iterators_arr = [str(x).strip().upper() for x in contexIterators.split(",") if x.strip()]

        if not self.exitsSemanticDimension(title):
            self.semanticDimensionsArr.append(
                SemanticDimensión(
                    _id,
                    str(title).upper(),
                    iterators_arr,
                    textSDimenDescript
                )
            )

    def exitsSemanticDimension(self, title):
        if not self.semanticDimensionsArr:
            return False

        for i in self.semanticDimensionsArr:
            if str(i.name) == title:
                return True

        return False

    def getSemanticDimsensionByTitle(self, title):
        _data = None
        try:
            for i in self.semanticDimensionsArr:
                if i.name == str(title).upper():
                    return i
        except:
            pass
        return _data

    def saveWork(self, title):
        _filename = self.config["output_file_tile"]
        _path = f"{self.path}/resources/teplate_vocabulary_tokenizer_ids.txt"
        _template = self.getTextInFile(_path)
        
        doc = ""
        ALL_VOCABULAY = ""
        VALUES = []
        for i in self.semanticDimensionsArr:
            # Documentation
            doc = doc + f"# {str(i.name).upper()} {str(i.contextualIteratorsArr)}"

            itterCon = ""
            for itterContextual in i.contextualIteratorsArr:
                itterCon = itterCon + f"\"{itterContextual}\": <ZERO-ARR>,\n"

            _value_data = f"#{str(i.name).upper()}\n{itterCon}"
            VALUES.append(_value_data)

        print(doc)
        for i in VALUES:
            ALL_VOCABULAY = ALL_VOCABULAY + f"{i}"

        print(ALL_VOCABULAY)

    def _getZeroArr(self, qty):
        return "[" + "0"*qty + "]"

    def getTextInFile(self, path):
        info = None
        try:
            f = open(path, 'r', encoding="utf-8")
            return f.read()
        except:
            return info
