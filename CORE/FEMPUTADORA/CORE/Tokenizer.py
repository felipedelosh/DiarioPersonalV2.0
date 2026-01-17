"""
FelipedelosH
2026
Tokenizer

Enter a str("TeXt WiTh Spaces, Numbers 123, And $imbols")
Retrun array of tokens lower case in order
["text", "with", "spaces", "numbers", "123", "and", "$", "imbols"]
"""
from CORE.UTILS.StringProcesor import StringProcesor

class Tokenizer:
    def __init__(self):
        self.string_processor = StringProcesor()

    def tokenize(self, text):
        txtArr = []

        try:
            txt = str(text).lower()
            for itterWords in str(txt).split(" "):
                _w = str(itterWords)

                for itterStrangerChar in self.string_processor._stranger_characters:
                    if itterStrangerChar in _w:
                        txtArr.append(itterStrangerChar)
                        _w = str(_w).replace(itterStrangerChar, "")

                txtArr.append(_w)
        except:
            pass

        return txtArr