import tkinter as tk
import window_main

container = tk.Tk()
container.title("Clients")
container.geometry("900x600")

window_main.Window(container)

container.mainloop()
