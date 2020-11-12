# here we will simply place some text using a 'label'
# 'label' is a widget in tkinter with which the user does not interact.

from tkinter import *

root = Tk()

# setting the Width X Height geometry functions
# with only geometry user would still be able to change the window size ase needed.
root.geometry("400x250")

# To fix thewindow to a particular min or max, we can use the minsize() and maxsize() attribute
# NOTE : The window will now cannot be scaled below the minsize() specified.
root.minsize(600, 500)

# In a similar way we can specify the maxsize
root.maxsize(800, 700)

#------------------------------
# Making a label

# making a label object
lbl1 = Label(text="This is some random text !!...")

# to print 'lbl1' we have to pack it, inorder to print it in the GUI
lbl1.pack()

root.mainloop()