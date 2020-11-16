#---------------------
# Menus and Submenus
#---------------------

# here we will only make simple menus and associate them with a command
# for submenus : refer file menus_and_submenus_2.py

from tkinter import *

root = Tk()
root.geometry("300x100")
root.title("Menus and Submenus")

# To make a menu we use tkinter widget 'Menu'
# we will make a Menu widget by name 'mymenu'
mymenu = Menu(root)

# Now we will add a command to mymenu using the 'add_command' attribute
#  the 'add_command' takes two parameters 'label' and 'command' :
#     label : specifies the command label
#     command : command specifies the custom function to be implemented

# defining func1 to be used in add_command
def func1():
    print(f"Triggered func1")

mymenu.add_command(label="File", command=func1)
# adding another few commands to the menu
mymenu.add_command(label="Edit", command=func1)
mymenu.add_command(label="Tools", command=func1)
mymenu.add_command(label="Help", command=func1)
mymenu.add_command(label="Quit", command=quit)

# Now we will configure the root using .config
# using which we will specify the menu of root to be 'mymenu'
root.config(menu=mymenu)

root.mainloop()