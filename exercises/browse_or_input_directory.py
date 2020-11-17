#---------------------------------
# Browse or Input  a Directory    
#---------------------------------

from tkinter import filedialog
from tkinter import *

root = Tk()
root.title("Browsing or Input a Directory")
root.geometry("700x500")

dir_image = PhotoImage(file=r"d:/icons pack/icons/directory_icon.png")
# NOTE : here we have used 'subsample' to make the png img small in size for icon.
#        specifying a parameter of 1 will give original size, increasing from 1 will reduce the image size.
small_dir_image = dir_image.subsample(30)

dir_val = StringVar()
dir_entry = Entry(root, textvariable=dir_val, width=70)
dir_entry.grid(row=0, column=0, padx=10, pady=5)

# making the list_dir function for the button in use
def list_dir():
    dir_name = filedialog.askdirectory()
    dir_val.set(dir_name)

# To put image to the left of the button we have used 'compund=LEFT'
# Also adding a command to browse input directory.
browse_button = Button(root, text="Select Folder", image=small_dir_image, compound=LEFT, width=100, height=13, command=list_dir)
browse_button.grid(row=0, column=1)
#----------------------------------------------------------------------
root.mainloop()

