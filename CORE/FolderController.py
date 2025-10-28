"""
FelipedelosH
2025

Folder Controller
"""
import os
from os import scandir

class FolderController:
    def __init__(self, path, timeUtil):
        self.path = path
        self.timeUtil = timeUtil
        self.generateFolders()

    def generateFolders(self):
        folders = [
            "DATA",
            "DATA\\RESOURCES",
            "DATA\\DIARIO", 
            f"DATA\\DIARIO\\{self.timeUtil.getCurrentYYYY()}",
            "DATA\\DREAMS",
            f"DATA\\DREAMS\\{self.timeUtil.getCurrentYYYY()}",
            "DATA\\PEOPLE",
            "DATA\\SENTIMIENTOS",
            f"DATA\\SENTIMIENTOS\\{self.timeUtil.getCurrentYYYY()}",
            "DATA\\NOTAS",
            "DATA\\RESULTADOANUAL",
            "DATA\\ACTIVIDADES",
            f"DATA\\ACTIVIDADES\\{self.timeUtil.getCurrentYYYY()}",
            "DATA\\ECONOMIA",
            f"DATA\\ECONOMIA\\{self.timeUtil.getCurrentYYYY()}",
            "DATA\\ECONOMIA\\CAJA",
            "DATA\\ECONOMIA\\DEBITOS",
            f"DATA\\ECONOMIA\\DEBITOS\\{self.timeUtil.getCurrentYYYY()}",
            "DATA\\DISTRIBUCIONTIEMPO",
            "DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO",
            f"DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\{self.timeUtil.getCurrentYYYY()}",
            "DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\HORARIO",
            f"DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\HORARIO\\{self.timeUtil.getCurrentYYYY()}",
            "DATA\\PERFIL",
            "DATA\\NEURONAS",
            "DATA\\USOS",
            "DATA\\DRUGS",
            f"DATA\\DRUGS\\{self.timeUtil.getCurrentYYYY()}",
            "DATA\\WORK",
            "DATA\\TEMP"
        ]

        for itterFolder in folders:
            routePath = os.path.join(self.path, itterFolder)
            if not os.path.isdir(routePath):
                os.mkdir(routePath)
