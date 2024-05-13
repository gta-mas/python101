from tkinter import *


def move_up(event):
    # label.place(x=label.winfo_x(), y=label.winfo_y()-10)
    canvas.move(photo_image, 0, -10)

def move_down(event):
    # label.place(x=label.winfo_x(), y=label.winfo_y()+10)
    canvas.move(photo_image, 0, 10)

def move_left(event):
    # label.place(x=label.winfo_x()-10, y=label.winfo_y())
    canvas.move(photo_image, -10, 0)

def move_right(event):
    # label.place(x=label.winfo_x()+10, y=label.winfo_y())
    canvas.move(photo_image, 10, 0)


window = Tk()
# window.geometry("500x500")
#
window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)
#
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)
#
# my_image = PhotoImage(file="C:\\Users\\Gabo\\PycharmProjects\\python101\\pngwing.png")
# label = Label(window, image=my_image)
#
# label.place(x=0, y=0)

# -----------------------------------------------------------------------------------------------

canvas = Canvas(window, width=500, height=500)
canvas.pack()

my_image = PhotoImage(file="C:\\Users\\Gabo\\PycharmProjects\\python101\\pngwing.png")
photo_image = canvas.create_image(0,0,image=my_image, anchor=NW)


window.mainloop()