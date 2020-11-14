#---------------
#  Using Frames
#---------------

from tkinter import *

root = Tk()
root.geometry("700x500")

# Making a frame f1 in root
f1 = Frame(root, bg="blue", borderwidth=8, relief=SUNKEN)

# making another frame in root
f2 = Frame(root, bg="yellow", borderwidth=8, relief=GROOVE)

# Making a label in frame f1
# and setting bg, fg and borderwidth
# and relief
l1 = Label(f1, text="This is a Label !!.....", bg="green", fg="blue", borderwidth=4, relief=SUNKEN)
l2 = Label(f2, text="This is a Label !!.....", bg="green", fg="blue", borderwidth=4, relief=SUNKEN)

# packing the frame
f1.pack(side=LEFT, fill=Y)
f2.pack(side=TOP, fill=X)
# packing the label
l1.pack(side=LEFT, pady=50)
l2.pack(side=LEFT, pady=50)

root.mainloop()