from tkinter import *


count = 0

def click():
    global count
    count += 1
    print("Congratulations, "+str(count)+" prosecution(s) complete!")

window = Tk()

photo = PhotoImage(file="Donald_Trump_mug_shot.png")

button = Button(window,
                text="Click for more impeachments!",
                command=click,
                font=("Comic Sans", 20),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="bottom",
                relief=RAISED,
                bd=10)
button.pack()




window.mainloop()













