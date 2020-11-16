#-------------------------
#  Menus and Submenus 2   
#-------------------------

# Making dropdown menus

from tkinter import *

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
# Making a Menu by name 'File' and adding it to the top 'menubar'
# for this we will use the 'add_command' and associating it with a command
m1 = Menu(menubar, tearoff=0) # without tearoff tou will notice a dotted line at the top of the dropdown menu, which is used to separate the dropdown menu from the main windown.
                              # which is useful in some particular case. To disable the tearoff and the dotted lines, use 'tearoff=0'.
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

# Now we will configure the root using .config
# using which we will specify the menu of root to be 'menubar'
root.config(menu=menubar)

root.mainloop()