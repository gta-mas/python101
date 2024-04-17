from tkinter import *


def submit():
    print("The temperature is: "+str(scale.get()) + " degrees C")


window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=500,
              orient=VERTICAL,
              font=("Impact", 20),
              tickinterval=10,
              # showvalue=False,    # hides current value if False
              # resolution=5,         # increment of slider
              troughcolor="#69EAFF",
              fg="#FF1C00",
              bg="black"

              )

scale.pack()
# scale.set()     # set current value of slider


button = Button(window,
                text="Submit",
                command=submit)
button.pack()




window.mainloop()