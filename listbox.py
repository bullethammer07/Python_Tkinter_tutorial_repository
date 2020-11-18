#-------------------------------------
#         ListBox in Tkinter          
#-------------------------------------

from tkinter import *

root = Tk()
root.geometry("700x500")
root.title("Listbox")

# Here we will make a blank Listbox
#   Attributes :
#     root – root window.
#     bg – background colour
#     fg – foreground colour
#     bd – border
#     height – height of the widget.
#     width – width of the widget.
#     font – Font type of the text.
#     highlightcolor – The colour of the list items when focused.
#     yscrollcommand – for scrolling vertically.
#     xscrollcommand – for scrolling horizontally.
#     cursor – The cursor on the widget which can be an arrow, a dot etc.

# Common methods :
#   yview – allows the widget to be vertically scrollable.
#   xview – allows the widget to be horizontally scrollable.
#   get() – to get the list items in a given range.
#   activate(index) – to select the lines with a specified index.
#   size() – return the number of lines present.
#   delete(start, last) – delete lines in the specified range.
#   nearest(y) – returns the index of the nearest line.
#   curseselection() – returns a tuple for all the line numbers that are being selected.

# The listbox offers four different selection modes through the selectmode option. 
# These are : 
#   SINGLE (just a single choice). 
#   BROWSE (same, but the selection can be moved using the mouse). 
#   MULTIPLE (multiple item can be choosen, by clicking at them one at a time). 
#   EXTENDED (multiple ranges of items can be chosen, using the Shift and Control keyboard modifiers). 
# 
# The default is BROWSE. Use MULTIPLE to get “checklist” behavior, and EXTENDED when the user would usually pick only one item, 
# but sometimes would like to select one or more ranges of items.
lbx = Listbox(root, selectmode=MULTIPLE)

# Inserting something  into the listbox using 'insert'
# here 'END' signifies the index, the item to be inserted will inserted at the END
lbx.insert(END, "Entry 1") # User can also specify indexes such as 1,2,3,4 in place of END
lbx.insert(1, "Entry 2")
lbx.insert(2, "Entry 3")
lbx.insert(3, "Entry 4")
lbx.insert(4, "Entry 5")

# making a button to submit values from the listbox

def get_vals():
    print("Button Pressed !!...")
    active_vals = lbx.get(ACTIVE)
    print(active_vals)
    
    # getting all selected items
    # curselection : Gets a list of the currently selected alternatives. The list contains the indexes 
    #                of the selected alternatives (beginning with 0 for the first alternative in the list).
    all_vals = lbx.curselection()
    print(all_vals)

Button(root, text="Submit", command=get_vals).pack()

lbx.pack()

#--------------------------------------
root.mainloop()