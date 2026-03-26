"""
FelipedelosH
2026
"""
import re
import json
import os
from os import scandir
from src.models.SemanticDimension import SemanticDimension
from src.models.Graph import Graph

class Controller:
    def __init__(self):
        self.path = os.getcwd()
        self._DATA_ = None

        # VARS
        self.semanticDimensionsArr = []
        self.finalPythonDataVocabularizer = [] # Save LINE TO LINE final code arr(str)
        self.keysContextualIterators = [] # str: storages all words
        self.sinapsis = Graph()
        self.pos_x_dimension = 0
        self.word_x_dimension = ""
        self.pos_y_dimension = 0
        self.word_y_dimension = ""

    def loadPreviosWorksNameSpaces(self):
        works = ["NEW"]

        try:
            output_dir = os.path.join(self.path, "OUTPUT")
            for file in os.listdir(output_dir):
                if file.endswith(".py"):
                    name = os.path.splitext(file)[0]
                    works.append(name)
        except:
            return works

        return works
    
    def loadPreviousWork(self, name):
        _status = self.loadVocabularyFromFile(name)
        if _status:
            self.semanticDimensionsArr = []
            self.finalPythonDataVocabularizer = []
            self.extractSemanticDimensionsFromPythonClassDoc()
            self.extractSemanticConectionsFromPythonClass()

        return _status
    
    def loadVocabularyFromFile(self, name):
        try:
            with open(f"{self.path}/OUTPUT/{name}.py", "r", encoding="UTF-8") as f:
                self._DATA_ = f.read()

            return True
        except:
            return False
        
    def getTextInFile(self, path):
        info = None
        try:
            f = open(path, 'r', encoding="utf-8")
            return f.read()
        except:
            return info
        
    def mouveUP(self):
        if self.pos_y_dimension - 1 >= 0:
            self.pos_y_dimension = self.pos_y_dimension - 1
            self.update_dimensional_keys_by_xy(self.pos_x_dimension, self.pos_y_dimension)
    def mouveDOWN(self):
        self.pos_y_dimension = self.pos_y_dimension + 1
        self.update_dimensional_keys_by_xy(self.pos_x_dimension, self.pos_y_dimension)
    def mouveRIGHT(self):
        self.pos_x_dimension = self.pos_x_dimension + 1
        self.update_dimensional_keys_by_xy(self.pos_x_dimension, self.pos_y_dimension)
    def mouveLEFT(self):
        if self.pos_x_dimension - 1 >= 0:
            self.pos_x_dimension = self.pos_x_dimension - 1
            self.update_dimensional_keys_by_xy(self.pos_x_dimension, self.pos_y_dimension)
    def update_dimensional_keys_by_xy(self, x, y):
        try:
            if len(self.keysContextualIterators) < x or len(self.keysContextualIterators) < y:
                return

            self.word_x_dimension = self.keysContextualIterators[x]
            self.word_y_dimension = self.keysContextualIterators[y]
        except:
            pass
        
    def setNewSemanticDimension(self, title, contexIterators, textSDimenDescript):
        _id = len(self.semanticDimensionsArr) + 1
        iterators_arr = [str(x).strip().lower() for x in contexIterators.split(",") if x.strip()]

        if not self.exitsSemanticDimension(title):
            self.semanticDimensionsArr.append(
                SemanticDimension(
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
    
    def getSemanticDimesionStatitics(self):
        return {
            "total": len(self.semanticDimensionsArr)
        }

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
                                self.keysContextualIterators.append(itterContextual)
                        self.semanticDimensionsArr[_semanticDimensionCounter].contextualIteratorsArr = _semanticDimensionContextualIteratorsArr

                    if " >> " not in itterLine:
                        #print(f"Documentacion Explain: {itterLine}")
                        _description = str(itterLine).split("# ")[1]
                        self.semanticDimensionsArr[_semanticDimensionCounter].description = _description

                        _semanticDimensionCounter = _semanticDimensionCounter + 1

                # Is Semantic info area?
                if itterLine == "vocabulary = {":
                    break

    def extractSemanticConectionsFromPythonClass(self):
        """
        Entrer a PYTHON CODE in TEXT
        Analized the weight conections to construct Sinaptic Graph
        """
        # STEP 0: READ ALL
        _isSemanticConectionsWeigthArea = False
        for i in self._DATA_.split("\n"):
            itterLine = str(i).strip()
            if  itterLine != "":
                # Is Semantic info area?
                if itterLine == "vocabulary = {":
                    _isSemanticConectionsWeigthArea = True
                    continue

                if itterLine == "}":
                    break
                
                if _isSemanticConectionsWeigthArea:
                    if itterLine[0] == "#":
                        #print(f"Doc: {itterLine}")
                        pass

                    if itterLine[0] != "#":
                        _data = str(itterLine).replace(" ", "")
                        _data = str(_data).split("\":[")
                        
                        _keyword = str(_data[0]).replace("\"", "")
                        self.sinapsis.addNode(_keyword)

        # STEP 0: FILL CONECTIONS DATA
        _isSemanticConectionsWeigthArea = False
        for i in self._DATA_.split("\n"):
            itterLine = str(i).strip()
            if  itterLine != "":
                # Is Semantic info area?
                if itterLine == "vocabulary = {":
                    _isSemanticConectionsWeigthArea = True
                    continue

                if itterLine == "}":
                    break
                
                if _isSemanticConectionsWeigthArea:
                    if itterLine[0] == "#":
                        #print(f"Doc: {itterLine}")
                        pass

                    if itterLine[0] != "#":
                        _data = str(itterLine).replace(" ", "")
                        _data = str(_data).split("\":[")
                        
                        _keyword = str(_data[0]).replace("\"", "")

                        _conectionValues = str(_data[1]).replace("\n", "")
                        _conectionValues = _conectionValues.replace("[", "")
                        _conectionValues = _conectionValues.replace("]", "")
                        _conectionValues = _conectionValues.replace("+", ",")
                        _conectionValues = _conectionValues[:-1]

                        """
                        If conection = 0 DONT Create.
                        """
                        _conter = 0
                        for itterConxtextualValue in str(_conectionValues).split(","):
                            if itterConxtextualValue != "0":
                                _targetValue = self.sinapsis.nodes[_conter]
                                #print(f"Para: {_keyword} en la pos: {_conter}:{_targetValue} el  valor es: {itterConxtextualValue}")
                                self.sinapsis.addEdge(_keyword, _targetValue, float(itterConxtextualValue))

                            _conter = _conter + 1

    def savePythonSemanticDimension(self, title):
        _pathTemplate = f"{self.path}/resources/template_vocabulary_tokenize_ids.txt"
        _template = self.getTextInFile(_pathTemplate)
        
        doc = ""
        _zeroCounter = 0
        _ZeroCounterArr = []
        _maxWorldLen = self.getMaxWordLen()
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
                key_text = f"\"{itterContextual}\":"
                key_text = key_text.ljust(_maxWorldLen + 3)
                itterCon += f"\t{key_text} <ZERO-ARR>,\n"

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

        self.finalPythonDataVocabularizer = _template.split("\n")
        self.setDiagonalOnesMatrix()
        self._savePythonFile(title)

    def _getZeroArr(self, qty):
        _zeroData = ", 0"*qty
        _zeroData = _zeroData[2::]

        return "[" + _zeroData + "]"

    def getMaxWordLen(self):
        _counter = 0
        for itterDimension in self.semanticDimensionsArr:
            for itterWord in itterDimension.contextualIteratorsArr:
                if len(itterWord) > _counter:
                    _counter = len(itterWord)

        return _counter
    
    def _isDetectedArrContextualIteratorsInLine(self, line):
        patron = r'^\s*"([^"]+)"\s*:\s*((?:\[[^\]]+\](?:\s*\+\s*\[[^\]]+\])*))\s*,\s*$'
        return re.match(patron, line)
    
    def setDiagonalOnesMatrix(self):
        _oneCounter = 0
        for idx, line in enumerate(self.finalPythonDataVocabularizer):
            match = self._isDetectedArrContextualIteratorsInLine(line)
            if match:
                new_line = self._setOneInArray(line, _oneCounter, match)
                self.finalPythonDataVocabularizer[idx] = new_line
                _oneCounter += 1

    def _setOneInArray(self, original_line, position, match):
        key = match.group(1)
        list_strings = match.group(2)
        start = match.start(2)
        end = match.end(2)
        prefix = original_line[:start]
        suffix = original_line[end:]

        blocks = list_strings.split(" + ")
        block_lengths = []
        all_numbers = []

        for block in blocks:
            nums = re.findall(r'[-+]?\d*\.?\d+', block)
            nums = [int(n) if '.' not in n else float(n) for n in nums]
            block_lengths.append(len(nums))
            all_numbers.extend(nums)

        if 0 <= position < len(all_numbers):
            all_numbers[position] = 1

        new_blocks = []
        idx = 0
        for length in block_lengths:
            block_nums = all_numbers[idx:idx+length]
            block_str = "[" + ", ".join(str(int(n) if isinstance(n, float) and n.is_integer() else n) for n in block_nums) + "]"
            new_blocks.append(block_str)
            idx += length

        new_list_strings = " + ".join(new_blocks)
        return prefix + new_list_strings + suffix

    def _savePythonFile(self, name):
        try:
            _path = f"{self.path}/OUTPUT/{name}.py"
            _data = ""

            for i in self.finalPythonDataVocabularizer:
                _data = _data + i + "\n"

            with open(_path,"w", encoding="UTF-8") as f:
                f.write(_data)
            print("SAVE PYTHON VOCABULARY")
        except:
            pass
