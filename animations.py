from tkinter import *
import time


WIDTH = 500
HEIGHT = 500
x_velocity = 3
y_velocity = 2

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

bg_image = PhotoImage(file="racetrack.png")
my_bgimage = canvas.create_image(0, 0, image=bg_image, anchor=NW)

photo_image = PhotoImage(file="pngwing.png")
my_image = canvas.create_image(0, 0, image=photo_image, anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0] >= (WIDTH-image_width) or coordinates[0] < 0):
        x_velocity = -x_velocity
    if (coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0):
        y_velocity = -y_velocity
    canvas.move(my_image, x_velocity, y_velocity)
    window.update()
    time.sleep(0.01)

window.mainloop()




