"""
FelipedelosH
2025
This is the main controller to load setting of config/config.json
"""
import json
import os

class ConfigManager:
    def __init__(self, config_path="config/config.json"):
        self.config_path = config_path
        self._data = {}
        self.load()

    def load(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, "r", encoding="utf-8") as f:
                self._data = json.load(f)
        else:
            self._data = {}

    def save(self):
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=4, ensure_ascii=False)

    def get(self, key, default=None):
        return self._data.get(key, default)

    def set(self, key, value):
        self._data[key] = value
        self.save()
