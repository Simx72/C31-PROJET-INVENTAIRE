
import tkinter as tk


class Heading1(tk.Frame):
    def __init__(self, parent, title):
        super().__init__(parent)

        # Main title
        self.title_label = tk.Label(self, text=title)
        self.title_label.pack()

        # Subtitle
        self.subtitle_label = tk.Label(self, text="")
        self.subtitle_label.pack()


class Heading2(tk.Frame):
    def __init__(self, parent, title):
        super().__init__(parent)

        self.heading2_label = tk.Label(self, text=title)
        self.heading2_label.pack()


class Heading3(tk.Frame):
    def __init__(self, parent, title):
        super().__init__(parent)

        self.heading3_label = tk.Label(self, text=title)
        self.heading3_label.pack()

class Heading4(tk.Frame):
    def __init__(self, parent, title):
        super().__init__(parent)

        self.heading4_label = tk.Label(self, text=title)
        self.heading4_label.pack()


class SearchBar(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.search_label = tk.Label(
            self,
            text="Rechercher un équipement"
        )
        self.search_label.pack()

        self.search_entry = tk.Entry(self)
        self.search_entry.pack()

        self.search_button = tk.Button(
            self,
            text="Rechercher"
        )
        self.search_button.pack()
