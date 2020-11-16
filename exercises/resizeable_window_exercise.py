#-----------------------------------------------------
# Description : Take Height and Width value from user 
#               and change the window size
#-----------------------------------------------------

from tkinter import *

root = Tk()
root.geometry("230x75")
root.title("Resizeable Window")

l1 = Label(root, text="Window Width   : ")
l2 = Label(root, text="Window Height  : ")

# packing l1 and l2 using grid
l1.grid()
l2.grid(row=1, column=0)

width_val = IntVar()
height_val = IntVar()

width_entry = Entry(root, textvariable=width_val).grid(row=0, column=1)
height_entry = Entry(root, textvariable=height_val).grid(row=1, column=1)

# function 'get_val'
def get_val():
    wid = width_val.get()
    hgt = height_val.get()
    
    print(f"Width : {wid} Height : {hgt}")
    # resizing the window
    root.minsize(wid, hgt)
    
# Button to submit
Button(text="Submit", command=get_val).grid(row=3)

root.mainloop()