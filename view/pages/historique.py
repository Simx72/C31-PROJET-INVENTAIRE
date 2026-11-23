import tkinter as tk
# import Controller as controller
class Historique(tk.Frame):
  def __init__(self, parent):
    tk.Frame.__init__(self, parent)


# tests
if __name__ == "__main__":
  root = tk.Tk()
  root.geometry("800x700")
  page = Historique(root)
  page.pack()
  tk.mainloop()