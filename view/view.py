import tkinter as tk
from tkinter import font as tkfont

class View(tk.Tk):
    container: tk.Frame
    frames: dict[str, tk.Frame]

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Source - https://stackoverflow.com/a/7557028
        # Posted by Bryan Oakley, modified by community. See post 'Timeline' for change history
        # Retrieved 2026-11-19, License - CC BY-SA 4.0

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

    def set_frames(self, frames: tuple[tk.Frame, ...]):
        for F in frames:
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")


    def show_frame(self, page_name: str):
        '''Show a frame for the given page name'''
        self.frames[page_name].tkraise()


if __name__ == "__main__":
    # Example
    class StartPage(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            label = tk.Label(self, text="This is the start page", font=controller.title_font)
            label.pack(side="top", fill="x", pady=10)
            button1 = tk.Button(self, text="Go to Page One",
                                command=lambda: controller.show_frame("PageOne"))
            button2 = tk.Button(self, text="Go to Page Two",
                                command=lambda: controller.show_frame("PageTwo"))
            button1.pack()
            button2.pack()
    class PageOne(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            label = tk.Label(self, text="This is page 1", font=controller.title_font)
            label.pack(side="top", fill="x", pady=10)
            button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
            button.pack()
    class PageTwo(tk.Frame):
        def __init__(self, parent, controller):
            tk.Frame.__init__(self, parent)
            self.controller = controller
            label = tk.Label(self, text="This is page 2", font=controller.title_font)
            label.pack(side="top", fill="x", pady=10)
            button = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
            button.pack()
    app = View()
    app.set_frames((StartPage, PageOne, PageTwo))
    app.show_frame("StartPage")
    app.mainloop()