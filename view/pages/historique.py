import tkinter as tk
from typing import TYPE_CHECKING
from controller import Controller

class Historique(tk.Frame):
    controller: Controller
    def __init__(self, parent: tk.Frame, controller: Controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller



# tests
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    page = Historique(root)
    tk.mainloop()