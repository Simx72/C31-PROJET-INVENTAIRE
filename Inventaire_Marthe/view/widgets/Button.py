import tkinter as tk;

class Button (tk.Frame):
  label: tk.Label
  entry: tk.Entry

  def __init__(self, parent, label):
    tk.Frame.__init__(self, parent)
    self.label = tk.Label(self, text=label)
    #  Pas fini
