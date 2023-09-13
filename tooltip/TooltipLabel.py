import tkinter as tk
from tkinter import ttk
from Tooltip import Tooltip


class TkTooltipLabel(tk.Label):
    def __init__(self, master, text_tooltip="default text", **kwargs):
        super().__init__(master, **kwargs)
        self._tooltip = Tooltip(self, text_tooltip)

    def set_tooltip_text(self, text):
        self._tooltip.set(text)


class TtkTooltipLabel(ttk.Label):
    def __init__(self, master, text_tooltip="default text", **kwargs):
        super().__init__(master, **kwargs)
        self._tooltip = Tooltip(self, text_tooltip)

    def set_tooltip_text(self, text):
        self._tooltip.set(text)
