#--------------------
# tkinter buttons    
#--------------------

from tkinter import *

root = Tk()
root.geometry("700x500")

# making a frame
f1 = Frame(root, borderwidth=6, bg="green", relief=SUNKEN)

# packing the frame
f1.pack(side=LEFT, anchor="nw")

# making a small function to print something
def print_stuff():
    print("This is some random stuff printed !!....")

# Making a Button
# NOTE : We can also associate an action with a button using 'command'
#        for eg : below we have associate 'command' with the function 'print_stuff' befined above
#                 This will make clicking button 'b1' call the function 'print_stuff'
b1 = Button(f1, fg="red", text="Click Me", command=print_stuff)
b1.pack(side=LEFT, padx=5, pady=5)

# Making few more buttons
b2 = Button(f1, fg="red", text="Click Me")
b2.pack(side=LEFT, padx=5, pady=5)

b2 = Button(f1, fg="red", text="Click Me")
b2.pack(side=LEFT, padx=5, pady=5)

b2 = Button(f1, fg="red", text="Click Me")
b2.pack(side=LEFT, padx=5, pady=5)

root.mainloop()