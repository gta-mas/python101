# text widged = functions like a text area, you can enter multiple lines of text

from tkinter import *


def submit():
    text_input = text.get("1.0", END)
    print(text_input)

window = Tk()

text = Text(window,
            bg="light yellow",
            font=("Ink Free", 10),
            height=10,
            width=30,
            padx=5,
            pady=5,
            fg="purple")
text.pack()

button = Button(window, command=submit, text="submit")
button.pack()



window.mainloop()