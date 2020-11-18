#-------------------------
#       Scrollbar         
#-------------------------

from tkinter import *

root = Tk()
root.geometry("700x500")
root.title("Scrollbar")

#--------------------------------------------------------------------------------------
# NOTE : To connect any widget to scrollbar you need to take care of two things :
#   1. make the 'yscrollcommand' of the widget equal to to the Scrollbat set() method.
#        -> widget(yscrollcommand = scrollbar.set)
#   2. make the 'command' of the Scrollbar equal to the widget's 'yview'
#        -> scrollbar.config(command=widget.yview)
#--------------------------------------------------------------------------------------

# making a scrollbar
sclbar = Scrollbar(root)
sclbar.pack(fill=Y, side=RIGHT)

# making a widget (Listbox here)
lbox = Listbox(root, yscrollcommand=sclbar.set)

# inserting a large number of items in the listbox
for i in range(500):
    lbox.insert(END, f"Item no {i}")

lbox.pack()
sclbar.config(command=lbox.yview)

#-----------------------------------
root.mainloop()