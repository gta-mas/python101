from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) # widget that manages a collection of windows and displays

tab1 = Frame(notebook)  # new frame for tab1
tab2 = Frame(notebook)

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both")     # expands to fill
                                            # fill fills the space on x/y axis

Label(tab1, text="Hello, this is tab1", width=50, height=25).pack()
Label(tab2, text="Goodbye, this is tab2", width=50, height=25).pack()

window.mainloop()



