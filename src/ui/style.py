import tkinter as tk
from tkinter import font

class UIConfig:
    """UI color and font configuration"""
    def __init__(self, root):
        self.colors = {
            'bg_primary': '#23272f',
            'bg_card': '#2c313c',
            'accent': '#4ecca3',
            'x_color': '#e06c75',
            'o_color': '#61afef',
            'text_primary': '#f8f8f2',
            'text_secondary': '#b2becd',
            'hover': '#3a3f4b',
            'success': '#4ecca3',
            'warning': '#f1c40f',
            'error': '#e74c3c',
        }
        self.fonts = {
            'title': font.Font(root=root, family="Segoe UI", size=16, weight="bold"),
            'score': font.Font(root=root, family="Segoe UI", size=10, weight="bold"),
            'button': font.Font(root=root, family="Segoe UI", size=18, weight="bold"),
            'turn': font.Font(root=root, family="Segoe UI", size=11, weight="normal"),
            'small': font.Font(root=root, family="Segoe UI", size=9),
            'symbol': font.Font(root=root, family="Segoe UI", size=32, weight="bold"),
        }
