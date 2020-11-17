#-----------------------------
#    Sliders using Scale()    
#-----------------------------

from tkinter import *

root = Tk()
root.title("Sliders")
root.geometry("350x300")

# Here we will add a Slider using Scale
# The slider below will be veritcal
my_slider = Scale(root, from_=0,  to=100) # the slider will pick values from 0-100

# to make a horizontal slider, use 'orient=HORIZONTAL'
my_slider2 = Scale(root, from_=0,  to=100, orient=HORIZONTAL)
# to start slider with an initial value, set it to value (as shown below)
# this will make slider to have range 0-100 but will start with the specified initial value.
my_slider2.set(20) # setting initial value to 20

def new_pos(val):
    print(f"new scale value is : {val}")

# making a slider that takes values only of specific intervals, use 'tickinterval'
my_slider3 = Scale(root, 
                   from_=0,  
                   to=100, 
                   orient=HORIZONTAL, 
                   tickinterval=20,
                   # label : You can display a label within the scale widget by setting this option to the label's text.
                   label="Slider 3 :",
                   
                   # length : The length of the scale widget. This is the x dimension if the scale is horizontal, or the y dimension if vertical.
                   #          The default is 100 pixels.
                   length=300,
                   
                   # sliderlength : Normally the slider is 30 pixels along the length of the scale.
                   #                You can change that length by setting the sliderlength option to your desired length.
                   sliderlength=20,
                   
                   # relief : Specifies the appearance of a decorative border around the label. The default is FLAT; for other values.
                   relief=RAISED,
                   
                   # activebackground : The background color when the mouse is over the scale.
                   activebackground="grey",
                   
                   # state : Set state=DISABLED to make the widget unresponsive.
                   #state=DISABLED, # UNCOMMENT TO RUN
                   
                   # bg : The background color of the parts of the widget that are outside the trough.
                   bg="grey",
                   
                   # bd : Width of the 3-d border around the trough and slider. Default is 2 pixels.
                   bd=5,
                   
                   # command : A procedure to be called every time the slider is moved. This procedure will be passed one argument, 
                   #           the new scale value. If the slider is moved rapidly, you may not get a callback for every possible position, 
                   #           but you'll certainly get a callback when it settles.
                   command=new_pos,
                   
                   # cursor : If you set this option to a cursor name (arrow, dot etc.), the mouse cursor will change to that pattern when it is over the scale.
                   cursor="arrow",
                   
                   # showvalue : Normally, the current value of the scale is displayed in text form by the slider 
                   #             (above it for horizontal scales, to the left for vertical scales). Set this option to 0 to suppress that label.
                   showvalue=0, # setting it to 0
                   
                   # width : The width of the trough part of the widget.
                   #         This is the x dimension for vertical scales and the y dimension if the scale has orient=HORIZONTAL. Default is 15 pixels.
                   width=30,
                   
                   # troughcolor : The color of the trough.
                   troughcolor="blue"
                   )

# making function get_val for button
def get_val():
    # getting the values from both sliders
    slider1_val = my_slider.get()
    slider2_val = my_slider2.get()
    slider3_val = my_slider3.get()
    print(f"Slider 1 value : {slider1_val}")
    print(f"Slider 2 value : {slider2_val}")
    print(f"Slider 3 value : {slider3_val}")

# We will make a button below to submit the values
bt1 = Button(text="Submit", command=get_val)

# packing the myslider
my_slider.pack()
my_slider2.pack()
my_slider3.pack()
bt1.pack()

root.mainloop()