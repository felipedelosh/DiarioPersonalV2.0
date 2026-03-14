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

    def prettyText(self, width, text):
        """
        Return a TEXT with constant width
        """
        if len(str(text)) == width:
            return str(text)
        elif len(str(text)) > width:
            return str(text)[:width - 3] + "..."
        else:
            return str(text) + " " * (width - len(str(text)))
        
    def prettyCurrency(self, cash):
        """
        Return a money with >$ and points
        """
        cash_str = str(cash).strip()

        if not cash_str:
            return "$0"

        prettyCash = ""
        _totalLenCash = len(cash_str)
        _counterTreeNumbers = 0

        while _totalLenCash > 0:
            if _totalLenCash == 1:
                prettyCash = cash_str[0] + prettyCash
                break

            _counterTreeNumbers = _counterTreeNumbers + 1
            pivot = cash_str[_totalLenCash - 1]

            if _counterTreeNumbers >= 3:
                prettyCash = "." + pivot + prettyCash
                _counterTreeNumbers = 0
            else:
                prettyCash = pivot + prettyCash

            _totalLenCash = _totalLenCash - 1

        return f"${prettyCash}"

    def validateTXT(self, txt):
        return str(txt).strip() != ""
