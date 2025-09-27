"""
FelipedelosH
2025
"""
import tkinter as tk
from abc import ABC, abstractmethod

class Screen(ABC):
    def __init__(self, master, manager):
        self.master = master
        self.manager = manager  
        self.canvas = tk.Canvas(self.master)

    @abstractmethod
    def render(self):
        pass

    def destroy(self):
        self.canvas.delete("all")
