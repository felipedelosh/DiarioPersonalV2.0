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
        
    def overWritefile(self, path, content):
        try:
            with open(path, "w", encoding="UTF-8") as f:
                f.write(content)

            return True
        except:
            return False
        
    def saveUsage(self, path, timeData):
        try:
            data = ""
            try:
                with open(path, 'r', encoding="UTF-8") as f:
                    data = f.read()
            except:
                pass

            with open(path, 'w', encoding="UTF-8") as f:
                if data == "":
                    f.write(timeData)
                else:
                    f.write(data+"\n"+timeData)

            return True
        except:
            return False
