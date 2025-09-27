"""
FelipedelosH
2025
"""
import tkinter as tk
from abc import ABC, abstractmethod

class Screen(ABC):
    def __init__(self, master, canvas, manager):
        self.master = master
        self.canvas = canvas
        self.manager = manager

    @abstractmethod
    def render(self, x, y):
        pass

    def destroy(self):
        try:
            self.canvas.delete("all")
        except Exception:
            pass
