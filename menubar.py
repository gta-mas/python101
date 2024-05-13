from tkinter import *
from tkinter import filedialog
from tkinter import *


def open_file():
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\Gabo\\PycharmProjects\\python101",
                                           title="Open File Pls",
                                           filetypes=(("text files", "*.txt"),
                                                      ("all files", "*.*")))
    file = open(file_path, "r")
    print(file.read())
    file.close()
    print("File has been opened!")


def save_file():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Gabo\\PycharmProjects\\python101",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("text files", ".txt"),
                                        ("HTML files", ".html"),
                                        ("all files", ".*"),
                                    ])
    if file is None:
        return

    # file_text = str(text.get(1.0, END))
    file_text = input("Enter text: ")
    file.write(file_text)
    file.close()
    print("File has been saved!")


def cut():
    print("You cut some text!")


def copy():
    print("You copied some text!")


def paste():
    print("You pasted some text!")

window = Tk()

# adding images next to the text
# open_image = PhotoImage(file="file path")
# save_image = PhotoImage(file="file path")
# exit_image = PhotoImage(file="file path")

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0, font=("MV Boli", 15))
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file) # image=open_image, compound="left"
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0, font=("MV Boli", 15))
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

window.mainloop()


