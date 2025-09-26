"""
FelipedelosH
2025
"""
class FileWriter:
    def __init__(self):
        pass

    def saveFile(self, path, content):
        try:
            print(f"Save: {path}, {content}")
            return True
        except:
            return False
