"""
FelipedelosH
2026
"""
import json
import os
from os import scandir
from src.models.SemanticDimension import SemanticDimension

class Controller:
    def __init__(self):
        self.path = os.getcwd()
        self._DATA_ = None

        # VARS
        self.semanticDimensionsArr = []

        if self.loadVocabularyFile():
            print("INFO::LOAD_VOCABULARY::OK")
            self.extractSemanticDimensionsFromPythonClassDoc()
    
    def loadVocabularyFile(self):
        try:
            with open(f"{self.path}/vocabulary_tokenizer_ids.py", "r", encoding="UTF-8") as f:
                self._DATA_ = f.read()

            return True
        except:
            return False


    def extractSemanticDimensionsFromPythonClassDoc(self):
        """
        Entrer a PYTHON CODE in TEXT
        Analized the previouly doc to extract all semeactic dimensions
        """
        _semanticDimensionCounter = 0

        for i in self._DATA_.split("\n"):
            itterLine = str(i).strip()
            if  itterLine != "":
                # Is Documentation
                if itterLine[0] == "#":
                    if " >> " in itterLine:
                        #print(f"Documentacion Header: {itterLine}")
                        tempSemanticDimension = SemanticDimension(_semanticDimensionCounter, "NEW", [], "")
                        self.semanticDimensionsArr.append(tempSemanticDimension)
                        _data = itterLine.split(" >> ")
                        _semanticDimensionName = str(_data[0]).split("# ")[1]
                        self.semanticDimensionsArr[_semanticDimensionCounter].name = str(_semanticDimensionName)

                        _semanticDimensionContextualIteratorsArrStr = str(_data[1])
                        _semanticDimensionContextualIteratorsArrStr = _semanticDimensionContextualIteratorsArrStr[1:]
                        _semanticDimensionContextualIteratorsArrStr = _semanticDimensionContextualIteratorsArrStr[:-1]

                        _semanticDimensionContextualIteratorsArr = []
                        for i in str(_semanticDimensionContextualIteratorsArrStr).split(","):
                            itterContextual = str(i).strip()
                            if itterContextual != "":
                                _semanticDimensionContextualIteratorsArr.append(itterContextual)
                        self.semanticDimensionsArr[_semanticDimensionCounter].contextualIteratorsArr = _semanticDimensionContextualIteratorsArr

                    if " >> " not in itterLine:
                        #print(f"Documentacion Explain: {itterLine}")
                        _description = str(itterLine).split("# ")[1]
                        self.semanticDimensionsArr[_semanticDimensionCounter].description = _description

                        _semanticDimensionCounter = _semanticDimensionCounter + 1

                # Is Semantic info area?
                if itterLine == "vocabulary = {":
                    break

    