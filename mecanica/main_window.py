from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

    def create_widgets(self):
        pass


container = Tk()
