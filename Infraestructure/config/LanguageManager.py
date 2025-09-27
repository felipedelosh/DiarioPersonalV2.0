"""
FelipedelosH
2025

Language Manager
"""
import json
import os

class LanguageManager:
    def __init__(self, base_path="ASSETS/LAN", lang="ES"):
        self.lang = lang
        self.base_path = f"{base_path}/{self.lang}.json"
        self.texts = {}
        self._load_language()

    def _load_language(self):
        if os.path.exists(self.base_path):
            with open(self.base_path, "r", encoding="utf-8") as f:
                self.texts = json.load(f)
        else:
            self.texts = {}

    def getText(self, key: str, default="") -> str:
        return self.texts.get(key, default)

    def set_lang(self, lang: str):
        self.lang = (lang or "ES").upper()
        self._load_language()

    def all_keys(self):
        return list(self.texts.keys())
