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
        self.finalPythonDataVocabularizer = ""
        self.pos_x_dimension = 0
        self.pos_y_dimension = 0

        self.loadPreviousWork()

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
        iterators_arr = [str(x).strip().lower() for x in contexIterators.split(",") if x.strip()]

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
        _zeroCounter = 0
        _ZeroCounterArr = []
        ALL_VOCABULAY = ""
        VALUES = []
        for i in self.semanticDimensionsArr:
            # Documentation
            iters_str = ", ".join(i.contextualIteratorsArr)
            doc = doc + f"# {str(i.name).upper()} >> [{iters_str}]\n# {i.description}\n"
            _zeroCounter = _zeroCounter + len(i.contextualIteratorsArr)
            _ZeroCounterArr.append(len(i.contextualIteratorsArr))
 
            itterCon = ""
            for itterContextual in i.contextualIteratorsArr:
                itterCon = itterCon + f"\t\"{itterContextual}\": <ZERO-ARR>,\n"

            _value_data = f"#{str(i.name).upper()}\n{itterCon}"
            VALUES.append(_value_data)

        zeroArr = ""
        for i in _ZeroCounterArr:
            zeroArr = zeroArr + f"{self._getZeroArr(i)} + "

        zeroArr = zeroArr[:-3]
        for i in VALUES:
            ALL_VOCABULAY = ALL_VOCABULAY + f"{str(i).replace("<ZERO-ARR>", zeroArr)}\n"

        ALL_VOCABULAY = ALL_VOCABULAY[:-2]
        _template = _template.replace("<SEMANTIC_FIELDS_DOCUMENTATION>", doc)
        _template = _template.replace("<ALL_VOCABULAY>", ALL_VOCABULAY)

        self.finalPythonDataVocabularizer = _template
        self.saveWorkJson(title)
        self._saveFiles()

    def _getZeroArr(self, qty):
        _zeroData = ", 0"*qty
        _zeroData = _zeroData[2::]

        return "[" + _zeroData + "]"

    def getTextInFile(self, path):
        info = None
        try:
            f = open(path, 'r', encoding="utf-8")
            return f.read()
        except:
            return info
        
    def _saveFiles(self):
        try:
            _path = f"{self.path}/OUTPUT/vocabulary_tokenizer_ids.py"
            with open(_path,"w", encoding="UTF-8") as f:
                f.write(self.finalPythonDataVocabularizer)
            print("SAVE PYTHON VOCABULARY")
        except:
            pass

    def saveWorkJson(self, title):
        try:
            _path = f"{self.path}/INPUT/temp.json"
            data = [d.to_dict() for d in self.semanticDimensionsArr]
            with open(_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            _path = f"{self.path}/INPUT/{title}.json"
            with open(_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print("Save WORK JSON")
            return True
        except Exception as e:
            print(f"ERROR saveWorkJson: {e}")
            return False

    def loadPreviousWork(self):
        try:
            _path = f"{self.path}/INPUT/temp.json"
            with open(_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.semanticDimensionsArr = [SemanticDimensión.from_dict(d) for d in data]
            print("LOAD WORK JSON")
            return True
        except Exception as e:
            print(f"ERROR loadPreviousWork: {e}")
            return False