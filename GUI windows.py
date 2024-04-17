from tkinter import *


# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() # instantiate an instance of a window
# window.geometry("420x420")
window.title("First GUI Program")

icon = PhotoImage(file="Donald_Trump_mug_shot.png")
window.iconphoto(True, icon)

window.config(background="black")

label = Label(window,                       # label = an area widget that holds text and/or an image within a window
              text="They are after you, I'm just in their way.",
              font=("Arial", 20, "bold"),
              fg="#00FF00",
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=icon,
              compound="bottom")
# label.place(x=0, y=210)
label.pack()


window.mainloop()   # places a window on a computer screen, listens for events


