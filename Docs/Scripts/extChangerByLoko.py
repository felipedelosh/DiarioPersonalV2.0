"""
FelipedelosH

Read all folders and then read all files and change extensions
"""
import os
from os import scandir
import shutil

_folders = []
_originalExt = ".xlsx"
_futureExt = ".csv"

if not os.path.isdir("CONVERT"):
    os.mkdir("CONVERT")

for itterFolder in scandir("."):
    if itterFolder.is_dir() and itterFolder.name != "CONVERT":
        _folders.append(itterFolder.name)

for itterFolder in _folders:
    for itterFile in scandir(itterFolder):
        if itterFile.is_file():
            if _originalExt in itterFile.name:
                if not os.path.isdir(f"CONVERT/{itterFolder}"):
                    os.mkdir(f"CONVERT/{itterFolder}")

                pathOutputFile = f"CONVERT/{itterFolder}/{str(itterFile.name).replace(_originalExt, _futureExt)}"
                shutil.copy2(itterFile.path, pathOutputFile)
                print(f"CONVERT: {pathOutputFile}")
