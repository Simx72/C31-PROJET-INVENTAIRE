#Importing libraries
import tkinter as tk

#creation de la vue (11-09)
class View:
    def __init__(self, root):
        self.root = root


    def create_title(self, parent, title):
        self.parent = parent

        #main frame
        self.main_frame = tk.Frame(self.parent)
        self.main_frame.pack()
        self.title = title
        #widget
        self.widget = tk.Frame(self.main_frame)
        self.widget.pack() #will add side, position, font, color etc

        #title display
        self.title_label = tk.Label(self.widget, text=title) #will add the rest later
        self.title_label.pack()

        #subtitle display
        self.subtitle_label = tk.Label(self.widget, text="") #will add font etc, text has to change depending on page. has to be right under title and tiny
        self.subtitle_label.pack()

    #Input
    def create_input(self, input_parent, input_label):
        self.input_parent = input_parent
        self.input_label = input_label

        self.input_frame = tk.Frame(input_parent)
        self.input_frame.pack()

        self.input_label = tk.Label(self.input_frame, text=input_label)

        self.input_entry = tk.Entry(self.input_frame)


        self.input_label.grid(row=0, column=0)
        self.input_entry.grid(row=0, column=1)


    #titre : Information de l'emprunteur
    def create_section_title(self, section_parent, section_title):
        self.section_title = tk.Frame(section_parent)
        self.section_title.pack()

        self.section_label = tk.Label(self.section_title, text=section_title)
        self.section_label.pack()

    # Search bar
    def create_search(self, search_parent):
        self.search_parent = search_parent
        self.search_frame = tk.Frame(search_parent)
        self.search_frame.pack()
        self.search_input = tk.Label(self.search_frame, text="Rechercher un équipement")

        self.search_entry = tk.Entry(self.search_frame)

        self.search_button = tk.Button(self.search_frame, text="Rechercher")


        self.search_input.grid(row=0, column=0)
        self.search_entry.grid(row=1, column=0)
        self.search_button.grid(row=1, column=1)

    def create_confirmation(self, confirmation_parent, confirmation_text):
        self.confirmation_parent = confirmation_parent
        self.confirmation_frame = tk.Frame(confirmation_parent)
        self.confirmation_frame.pack()

        self.confirmation_button = tk.Button(self.confirmation_frame, text=confirmation_text)
        self.confirmation_button.grid(row=0, column=0)

    def create_cancelation(self, cancelation_parent):
        self.cancelation_parent = cancelation_parent
        self.cancelation_frame = tk.Frame(cancelation_parent)
        self.cancelation_frame.pack()

        self.cancel_button = tk.Button(self.cancelation_frame, text="Annuler")
        self.cancel_button.grid(row=1, column=0)

# emprunt ----------------------------------------
    def create_borrow_page(self, borrow_parent):
        self.borrow_parent = borrow_parent
        self.borrow_frame = tk.Frame(borrow_parent)
        self.borrow_frame.pack()

        #reuse other methods
        self.create_title(self.borrow_frame, "Emprunt d'équipement")

        self.create_section_title(self.borrow_frame, "Information de l'emprunteur")

        self.create_input(self.borrow_frame, "Nom : ")
        self.create_input(self.borrow_frame, "Prénom : ")
        self.create_input(self.borrow_frame, "No. d'identifiant : ")
        self.create_input(self.borrow_frame, "Status : ")

        self.create_section_title(self.borrow_frame, "Rechercher un équipement")
        self.create_search(self.borrow_frame)

        self.create_input(self.borrow_frame, "Date de l'emprunt (JJ-MM-AAAA) :")
        self.create_confirmation(self.borrow_frame, "Confirmer l'emprunt")
        self.create_cancelation(self.borrow_frame)
# retour ----------------------------------------
    def create_return_page(self, return_parent):
        self.return_parent = return_parent
        self.return_frame = tk.Frame(return_parent)
        self.return_frame.pack()

        #reuse other methods
        self.create_title(self.return_frame, "Retour d'équipement")
        self.create_search(self.return_frame)
        self.create_section_title(self.return_frame, "Information de l'emprunteur")
        self.create_input(self.return_frame, "No. d'identifiant : ")
        self.create_input(self.return_frame, "No. d'équipement : ")

        self.create_section_title(self.return_frame, "Pret sélectionné ")

        self.create_input(self.return_frame, "Équipement : ")
        self.create_input(self.return_frame, "Emprunteur : ")
        self.create_input(self.return_frame, "Date de l'emprunt (jj/mm/aa) : ")

        self.create_section_title(self.return_frame, "Date du retour")
        #local date time JJ/MM/AAAA

        self.create_confirmation(self.return_frame, "Confirmer le retour")
        self.create_cancelation(self.return_frame)
# adding equipment ----------------------------------------
    def create_add_equip(self, equip_parent):
        self.equip_parent = equip_parent
        self.equip_frame = tk.Frame(equip_parent)
        self.equip_frame.pack()

        self.create_title(self.equip_frame, "Ajouter un équipement")

        self.create_section_title(self.equip_frame, "Information de l'équipement")

        self.create_input(self.equip_frame, "Identifiant unique : ")
        self.create_input(self.equip_frame, "Nom de l'équipement : ")
        self.create_input(self.equip_frame, "Catégorie : ")
        self.create_input(self.equip_frame, "Description (facultative) : ")

        self.create_confirmation(self.equip_frame, "Confirmer")
        self.create_cancelation(self.equip_frame)
# removing equipment ----------------------------------------
    def create_remove_equip(self, equip_parent):
        self.equip_parent = equip_parent
        self.equip_frame = tk.Frame(equip_parent)
        self.equip_frame.pack()

        self.create_title(self.equip_frame, "Retirer un équipement")
        self.create_section_title(self.equip_frame, "Information de l'equipement")

        self.create_input(self.equip_frame, "Identifiant : ")
        self.create_input(self.equip_frame, "Nom de l'equipement : ")
        self.create_input(self.equip_frame, "Numéro de serie : ")

        self.create_confirmation(self.equip_frame, "Confirmer")
        self.create_cancelation(self.equip_frame)

# equipment consultation ----------------------------------------
    def create_consult_page(self, cons_parent, cons_remove_btn, cons_add_btn, cons_sorting_ctrl):
        self.cons_parent = cons_parent
        self.cons_frame = tk.Frame(cons_parent)
        self.cons_frame.pack()

        self.search_frame = tk.Frame(self.cons_parent)
        self.search_frame.pack()
        self.search_input = tk.Entry(self.cons_frame)
        self.search_button = tk.Button(self.cons_frame, text="Rechercher")
        self.search_input.grid(row=0, column=0)
        self.search_button.grid(row=0, column=1)

        self.cons_remove_btn = cons_remove_btn
        self.cons_remove_btn_frame = tk.Button(self.cons_remove_btn, text="Retirer un équipement")
        self.cons_remove_btn.grid(row=1, column=0)

        self.cons_add_btn = cons_add_btn
        self.cons_add_btn_frame = tk.Button(self.cons_add_btn, text="Ajouter un équipement")
        self.cons_add_btn.grid(row=2, column=0)
        self.cons_add_btn_frame.grid(row=2, column=1)

        self.cons_sorting_ctrl = cons_sorting_ctrl
        self.cons_sorting_ctrl_frame = tk.Frame(self.cons_parent)
        self.cons_sorting_ctrl_frame.pack()




#tkinter window
root = tk.Tk()
root.geometry("500x400")

#object
view = View(root)


view.create_borrow_page(root)
view.create_return_page(root)
view.create_add_equip(root)

root.mainloop()

