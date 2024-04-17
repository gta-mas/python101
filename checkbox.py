from tkinter import *


def display():
    if x.get() == 1:
        print("You are gay!")
    else:
        print("You are not gay!")



window = Tk()

x = IntVar()
photo = PhotoImage(file="u_are_gay.png")


check_button = Checkbutton(window,
                           text="I agree.",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=("Arial", 20),
                           fg="#00FF00",
                           bg="black",
                           activeforeground="#00FF00",
                           activebackground="black",
                           padx=20,
                           pady=20,
                           image=photo,
                           compound="left")


check_button.pack()


window.mainloop()