import tkinter as tk
class ConfirmationButton(tk.Frame):
    def __init__(self, parent, text, command):
        super().__init__(parent)

        self.confirm_button = tk.Button(
            self,
            text=text,
            command=command
        )
        self.confirm_button.pack()

class CancelButton(tk.Frame):
    def __init__(self, parent, text, command):
        super().__init__(parent)

        self.cancel_button = tk.Button(
            self,
            text=text,
            command=command
        )
        self.cancel_button.pack()



