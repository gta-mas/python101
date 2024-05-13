from tkinter import *


def do_something(event):
    # print("You pressed: " + event.keysym)
    # label.config(text=event.keysym)
    print("Mouse coordinates: " + str(event.x)+", "+str(event.y))

window = Tk()

# window.bind("<Key>", do_something)    # almost any keyboard key
# window.bind("<Button-1>", do_something) # LMB
# window.bind("<Button-2>", do_something) # MMB
# window.bind("<Button-3>", do_something) # RMB
# window.bind("<ButtonRelease>", do_something)
# window.bind("<Enter>", do_something)  # when you enter a window, event triggers
# window.bind("<Leave>", do_something)  # leave the window
window.bind("<Motion>", do_something)   # where the mouse moved
label = Label(window, font=("Helvetica", 100))
label.pack()



window.mainloop()




