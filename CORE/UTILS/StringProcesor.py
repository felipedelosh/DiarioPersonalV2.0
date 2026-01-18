"""
FelipedelosH
2025
"""
class StringProcesor:
    def __init__(self):
        self._numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self._accented_vowels = ["á", "é", "í", "ó", "ú"]
        self._str_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self._stranger_characters = [',', '#', '%', '?', '*', ':', "\\", '\n', '(', ')', "\'", '$', '>', '-', '[', ']', '+', '.', '#']

    def validateTXT(self, txt):
        return str(txt).strip() != ""
