import tkinter as tk
from Inventaire_Marthe.widgets.headers import Heading1, Heading2, Heading3, Heading4, SearchBar
from Inventaire_Marthe.widgets.buttons import ConfirmationButton, CancelButton
from Inventaire_Marthe.widgets.inputs import Input

class View:
    def create_add_equip(self, equip_parent):
        self.equip_parent = equip_parent
        self.equip_frame = tk.Frame(equip_parent)
        self.equip_frame.pack(fill="both", expand=True)

        #titres
        heading1 = Heading1(self.equip_frame, "Gestion des équipements")
        heading1.pack()

        heading2 = Heading2(self.equip_frame, "Ajouter un équipement")
        heading2.pack()

        heading3 = Heading3(self.equip_frame, "Information de l'équipement")
        heading3.pack()


        #new equip infos
        self.equip_id_input = Input(self.equip_frame, "Identifiant unique : ")
        self.equip_id_input.pack()

        self.equip_name_input = Input(self.equip_frame, "Nom de l'équipement : ")
        self.equip_name_input.pack()

        self.category_input = Input(self.equip_frame, "Catégorie : ")
        self.category_input.pack()

        confirm_btn = ConfirmationButton(self.equip_frame, "Confirmer l'ajout", command=lambda: print("Confirmé"))
        confirm_btn.pack()
                
        cancel_btn = CancelButton(self.equip_frame, "Annuler" ,command=lambda: print("Annulé"))
        cancel_btn.pack()


# Temporary test window
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")

    view = View()
    view.create_add_equip(root)

    root.mainloop()




