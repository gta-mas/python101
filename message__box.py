from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title="Info message box", message="You suck!")
    # messagebox.showwarning(title="WARNING!", message="You have a virus!")
    # messagebox.showerror(title="Error message box", message="You f'ed up!")
    # if messagebox.askokcancel(title="Ask Ok Cancel", message="Are you sure about this?") == True:
    #     print("You did it!")
    # else:
    #     print("You did not do it!")
    # if messagebox.askretrycancel(title="Ask Retry Cancel", message="Retry?") == True:
    #     print("You did it!")
    # else:
    #     print("You did not do it!")
    # if messagebox.askyesno(title="Ask Yes/No", message="Are you gay?"):
    #     print("You are gay")
    # else:
    #     print("You are not gay")
    # answer = messagebox.askquestion(title="Ask Question", message="Are you gay?")
    # if answer == "yes":
    #     print("You are gay!")
    # else:
    #     print("You are not gay!")
    answer = messagebox.askyesnocancel(title="Ask Yes/no/Cancel", message="Do you like gays?", icon="warning")
    if answer == True:
        print("You are most likely gay too!")
    elif answer == False:
        print("You are a trad man/woman")
    else:
        print("You have dodged this one!")

window = Tk()

button = Button(window,
                command=click,
                text="Click me!")
button.pack()


window.mainloop()