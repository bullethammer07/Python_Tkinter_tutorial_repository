#---------------------------------------------------
#           Events in Tkinter                       
#---------------------------------------------------

# NOTE : Visit site : https://effbot.org/tkinterbook/tkinter-events-and-bindings.htm for details of different events in tkinter
#        also refer documentation.

from tkinter import *

root = Tk()
root.title("Events in Tkinter")
root.geometry("700x500")

# Making function 'get_val' for button
def button_beh():
    pass

# NOTE : The function (below) has been specified with bind.
#        these functions take the event as the input argument.
#        below we have specifed the event as 'evt', this can be specified with any name
def click_beh(evt):
    # NOTE : We can use the attributes 'x' and 'y' of the event argument specified 'evt'
    #        the 'x' and 'y' return the coordinates where the click was made
    print(f"Button Clicked !!... {evt.x , evt.y}")
    
# Making function for hovering or entering into the button area
def btn_hover(evt):
    print(f"Coordinates : {evt.x , evt.y}")

# Making a button
# NOTE : here we have specified a color using 'activebackground' for what happens when the button is clicked.
#        highlight options can be specified using : highlightbackground, highlightcolor and highlightthickness. refer documentation for more details.
bt1 = Button(root, text="Click Me", padx=10, pady=10, command=button_beh, bg="yellow", activebackground='#696969')
bt1.pack()

# Binding clicking of left mouse button event to the widget
bt1.bind("<Button-1>", func=click_beh)
# binding hovering of pointer event to the widget
bt1.bind("<Enter>", func=btn_hover)

root.mainloop()