import Tkinter as Tk

#  frame that holds widgets to move the arm
from axes_panel import AxesPanel


class MoveFrame(Tk.Frame):
    def __init__(self, parent, **kw):
        Tk.Frame.__init__(self, parent, **kw)
        self._axes_panel = AxesPanel(self)
        self._axes_panel.pack()
