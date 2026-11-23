import tkinter as tk
from typing import TYPE_CHECKING
from Inventaire_Marthe.widgets.headers import Heading1, Heading2, Heading3, Heading4, SearchBar # type: ignore
from Inventaire_Marthe.widgets.buttons import ConfirmationButton, CancelButton # type: ignore
from Inventaire_Marthe.widgets.inputs import Input # type: ignore

if TYPE_CHECKING:
    from controller import Controller

class Inventaire:

    def __init__(self, inventory_parent, controleur: Controller): # type: ignore
        self.inventory_parent = inventory_parent # type: ignore
        self.inventory_frame = tk.Frame(inventory_parent) # type: ignore
        self.inventory_frame.pack(fill="both", expand=True)

        #Titles
        heading1 = Heading1(self.inventory_frame, "Gestion des équipements")
        heading1.pack()

        heading2 = Heading2(self.inventory_frame, "Inventaire des équipements")
        heading2.pack()

        #equipment rows
        # id row
        self.inventory_id_frame = inventory_id_frame
        self.inventory_id_frame = tk.Frame(inventory_parent)
        self.inventory_id_frame.pack()

        # equip name frame
        self.inventory_equip_name = inventory_equip_name_frame
        self.inventory_equip_name = tk.Frame()
        

        

        

        






# Temporary test window
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")

    view = Inventaire()
    view.create_inventory(root) # type: ignore

    root.mainloop()


 