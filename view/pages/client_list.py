import tkinter as tk
class Liste_client(tk.Frame):
  def __init__(self, parent):
    tk.Frame.__init__(self, parent)




# tests
if __name__ == "__main__":
  root = tk.Tk()
  root.geometry("600x400")
  page = Liste_client(root)

  tk.mainloop()