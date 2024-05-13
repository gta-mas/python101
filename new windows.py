from tkinter import *

def create_window():
    new_window = Tk()       # Toplevel() # = new window "on top" of other windows, linked to a "bottom" window (Tk() is the bottom window)
                            # Tk() = new independent window, not linked to a bottom window

    old_window.destroy()    # close out of the old window

old_window = Tk()

button = Button(old_window, text="Create New Window", command=create_window).pack()


old_window.mainloop()