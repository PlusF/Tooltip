import tkinter as tk
from Tooltip import Tooltip


class TooltipLabel(tk.Label):
    def __init__(self, master, text_tooltip="default tooltip", **kwargs):
        super().__init__(master, **kwargs)
        self._tooltip = Tooltip(self, text_tooltip)

    def set_tooltip_text(self, text):
        self._tooltip.set(text)
