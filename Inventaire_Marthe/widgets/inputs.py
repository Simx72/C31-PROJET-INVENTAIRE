import tkinter as tk
class Input(tk.Frame):
    def __init__(self, input_parent, input_label):
        super().__init__(input_parent)
       

        self.input_label = tk.Label(self, text=input_label)
        self.input_entry = tk.Entry(self)

        self.input_label.grid(row=0, column=0)
        self.input_entry.grid(row=0, column=1)

