from tkinter import *
from tkinter import filedialog


def save_file():
    file = filedialog.asksaveasfile(initialdir= "C:\\Users\\Gabo\\PycharmProjects\\python101",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("text files", ".txt"),
                                        ("HTML files", ".html"),
                                        ("all files", ".*"),
                                    ])
    if file is None:
        return
    file_text = str(text.get(1.0, END))
    # file_text = input("Enter text: ")
    file.write(file_text)
    file.close()


window = Tk()

button = Button(window,
                text="save",
                command=save_file)
button.pack()

text = Text(window)
text.pack()

window.mainloop()