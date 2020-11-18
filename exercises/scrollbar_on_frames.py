#-------------------------
#   Scrollbar on Frames   
#-------------------------

from tkinter import *

root = Tk()
root.geometry("200x300")
root.title("Scrollbar on Frames")

# Making two frames in the GUI
f1 = Frame(root, bg="blue", borderwidth=2, relief=SUNKEN)
f2 = Frame(root, bg="blue", borderwidth=2, relief=GROOVE)

# making scrollbars for the listboxes
lb1_sb = Scrollbar(f1)
lb2_sb = Scrollbar(f2)

# adding a listbox to frame f1 and f2
lbx1 = Listbox(f1, selectmode=MULTIPLE, yscrollcommand=lb1_sb.set)
lbx2 = Listbox(f2, selectmode=MULTIPLE, yscrollcommand=lb2_sb.set)

# adding to the configs of the scrollbars
lb1_sb.config(command=lbx1.yview)
lb2_sb.config(command=lbx2.yview)

# packing the scrollbars
lb1_sb.pack(side=RIGHT, fill=Y)
lb2_sb.pack(side=RIGHT, fill=Y)

# adding a lot of items to both the listboxes
for i in range(500):
    lbx1.insert(END, f"Listbox 1 insert item {i}")
    lbx2.insert(END, f"Listbox 2 insert item {i}")

f1.pack(side=TOP)
f2.pack(side=TOP)
lbx1.pack()
lbx2.pack()

#--------------------------------------------------
root.mainloop()