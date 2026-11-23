import tkinter as tk

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller import Controller

class MainMenu(tk.Frame):
    def __init__(self, parent: tk.Frame, controller: Controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.title = tk.Label(self, text="Menu principal")
        self.title.pack()

        page_buttons: dict[str, str] = {
            "equipements": "Équipements",
            "historique": "Historique",
            "clients": "Clients",
            "logout": "Déconnexion"
        }

        for page_id, page_btn_name in page_buttons.items():
            print(f"setting {page_id} : {page_btn_name}")
            btn = tk.Button(self, text=page_btn_name, command=self.make_btn_command(page_id))
            btn.pack()

    def make_btn_command(self, id: str):
        return lambda: print(f"Open {id}")

# tests
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    page = MainMenu(root, None)
    page.pack()
    tk.mainloop()