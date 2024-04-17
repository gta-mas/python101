from tkinter import *

food = ["president", "businessman", "philantrope"]

def order():
    if x.get() == 0:
        print("You ordered a president #MAGA!")
    elif x.get() == 1:
        print("You ordered a businessman")
    elif x.get() == 2:
        print("You ordered a philantrope")
    else:
        print("FJB!!!")


window = Tk()

president_image = PhotoImage(file="Donald_Trump_mug_shot.png")
businessman_image = PhotoImage(file="Donald_Trump_mug_shot.png")
philantrope_image = PhotoImage(file="Donald_Trump_mug_shot.png")
trump_images = [president_image, businessman_image, philantrope_image]


x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],    # adds text to radio buttons
                               variable=x,          # groups RBs together if they share the same variable
                               value=index,         # assigns each RB a different value
                               padx=25,
                               font=("impact", 50, "bold"),
                               image=trump_images[index], # adds image to RB and their respective index
                               compound="left",
                               indicatoron=False,   # eliminates circle indicator
                               width=750,           # sets width of RBs
                               command=order        # sets command of RB to function
                               )




    radio_button.pack(anchor=W)



window.mainloop()