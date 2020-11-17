#-----------------
#  Message Boxes  
#-----------------

from tkinter import *
# importing message boxes from tkinter
import tkinter.messagebox as mbox

root = Tk()
root.geometry("300x100")
root.title("Menus and Submenus")

# Menubar is like the complete set of menu available on top. It will Contain all objects like 'File' 'Edit' 'View' 'Help' etc
menubar = Menu(root)

# defining function 'func1' to be used below
def func1():
    pass

#-----------------------------------------------------------------------------
#                ***** Menu for "File" inside the top menu *****              
#-----------------------------------------------------------------------------
m1 = Menu(menubar, tearoff=0)
m1.add_command(label="New Project", command=func1)
m1.add_command(label="New", command=func1)
m1.add_command(label="Save", command=func1)
# Adding a separator line after Svae
m1.add_separator()
m1.add_command(label="Save As", command=func1)

# Now we will add the 'm1' menu to 'menubar' using 'add_cascade' and labelling the Menu as 'File'
menubar.add_cascade(label="File", menu=m1)

#-----------------------------------------------------------------------------
#                ***** Menu for "Edit" inside the top menu *****              
#-----------------------------------------------------------------------------
m2 = Menu(menubar, tearoff=0)
m2.add_command(label="Cut", command=func1)
m2.add_command(label="Copy", command=func1)
# Adding a separator line after Svae
m2.add_separator()
m2.add_command(label="Paste", command=func1)
m2.add_command(label="Delete", command=func1)

# Now we will add the 'm2' menu to 'menubar' using 'add_cascade' and labelling the Menu as 'Edit'
menubar.add_cascade(label="Edit", menu=m2)

#-------------------------------------------------
# Adding another menu by the name 'Help'
#-------------------------------------------------

# function for helpme
def helpme():
    msg_box = mbox.askquestion(title="Help", message="Would you like to enter the Help Webpage ?")
    # the object 'msg_box' contains the output of the message boc as specified by the user
    print(msg_box)

m3 = Menu(menubar, tearoff=0)
m3. add_command(label="Help", command=helpme)

menubar.add_cascade(label="Help", menu=m3)

#-------------------------------------------------
# Adding another menu by the name 'About'
#-------------------------------------------------
def about_us_dialog():
    # print("Message Box")
    msg_box = mbox.showinfo(title="About Us", message="Version 1.0")
    print(msg_box)

menubar.add_command(label="About", command=about_us_dialog)

# Now we will configure the root using .config
# using which we will specify the menu of root to be 'menubar'
root.config(menu=menubar)
root.mainloop()