import tkinter as tk


class Tooltip:
    def __init__(self, widget, text="default tooltip"):
        self._widget = widget
        self._text = text
        self._widget.bind("<Enter>", self._enter)
        self._widget.bind("<Motion>", self._motion)
        self._widget.bind("<Leave>", self._leave)
        self._id = None
        self._tw = None

    def _enter(self, event):
        self._schedule()

    def _motion(self, event):
        self._unschedule()
        self._schedule()

    def _leave(self, event):
        self._unschedule()
        self._id = self._widget.after(500, self._hide)

    def _schedule(self):
        if self._tw:
            return
        self._unschedule()
        self._id = self._widget.after(500, self._show)

    def _unschedule(self):
        _id = self._id
        self._id = None
        if _id:
            self._widget.after_cancel(_id)

    def _show(self):
        _id = self._id
        self._id = None
        if _id:
            self._widget.after_cancel(_id)
        x, y = self._widget.winfo_pointerxy()
        self._tw = tk.Toplevel(self._widget)
        self._tw.wm_overrideredirect(True)
        self._tw.geometry(f"+{x + 10}+{y + 10}")
        label = tk.Label(self._tw, text=self._text, background="lightyellow",
                         relief="solid", borderwidth=1, justify="left")
        label.pack(ipadx=10)

    def _hide(self):
        _tw = self._tw
        self._tw = None
        if _tw:
            _tw.destroy()

    def set(self, text):
        self._text = text
