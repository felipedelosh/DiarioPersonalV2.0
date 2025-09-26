"""
FelipedelosH
2025
"""
class FileWriter:
    def __init__(self):
        pass

    def saveFile(self, path, content):
        try:
            with open(path, "a", encoding="UTF-8") as f:
                f.write(content)

            return True
        except:
            return False
