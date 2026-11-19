from typing import TYPE_CHECKING 
from view.pages.login import Login
import tkinter as tk
from tkinter import font as tkfont

if TYPE_CHECKING:
    from controller import Controller

PAGES: tuple[tk.Frame, ...] = (Login,)

class View(tk.Tk):
    controller: Controller
    container: tk.Frame
    frames: dict[str, tk.Frame]

    def __init__(self, controller: Controller, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.controller = controller

        self.geometry("1200x800")

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

        if len(PAGES) == 0:
            print("Error: PAGES is empty.")
            exit(1)

        self.frames = {}
        self.set_frames(PAGES)
        self.show_frame(PAGES[0].__name__)

    def set_frames(self, frames: tuple[tk.Frame, ...]):
        for F in frames:
            page_name = F.__name__
            frame = F(parent=self.container, controller=self.controller)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")


    def show_frame(self, page_name: str):
        '''Show a frame for the given page name'''
        self.frames[page_name].tkraise()
    