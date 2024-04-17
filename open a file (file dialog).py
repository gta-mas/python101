from tkinter import *
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\Gabo\\PycharmProjects\\python101",
                                           title="Open File Pls",
                                           filetypes=(("text files", "*.txt"),
                                           ("all files", "*.*")))
    file = open(file_path, "r")
    print(file.read())
    file.close()



window = Tk()

button = Button(window,
                text="Open",
                command=open_file)
button.pack()



window.mainloop()