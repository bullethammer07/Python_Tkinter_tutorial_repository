#---------------------------------
# Browse or Input  a Directory    
#---------------------------------

from tkinter import filedialog
from tkinter import *

root = Tk()
root.title("Browsing or Input a Directory")
root.geometry("570x150")

# Directory Image
dir_image = PhotoImage(file=r"./../imgs/directory_icon.png")
# NOTE : here we have used 'subsample' to make the png img small in size for icon.
#        specifying a parameter of 1 will give original size, increasing from 1 will reduce the image size.
small_dir_image = dir_image.subsample(30)

# File Image
file_image = PhotoImage(file=r"./../imgs/file_icon_blue.png")
small_file_image = file_image.subsample(30)

dir_val = StringVar()
dir_entry = Entry(root, textvariable=dir_val, width=70)
dir_entry.grid(row=0, column=0, padx=10, pady=5)

file_val = StringVar()
file_entry = Entry(root, textvariable=file_val, width=70)
file_entry.grid(row=1, column=0, padx=10, pady=5)

# making the list_dir function for the button in use
def list_dir():
    dir_name = filedialog.askdirectory()
    dir_val.set(dir_name)

# making the list_file function for the button in use
def list_file():
    file_name = filedialog.askopenfilename()
    file_val.set(file_name)

# bottom right image logo
br_logo = PhotoImage(file=r"./../imgs/micron_logo.png")
small_br_logo = br_logo.subsample(25)

lba1 = Label(image=small_br_logo)
lba1.grid(row=2, column=1)

# To put image to the left of the button we have used 'compund=LEFT'
# Also adding a command to browse input directory.
dir_browse_button = Button(root, text="Select Folder", image=small_dir_image, compound=LEFT, width=100, height=13, command=list_dir)
dir_browse_button.grid(row=0, column=1)

file_browse_button = Button(root, text="  Select File  ", image=small_file_image, compound=LEFT, width=100, height=13, command=list_file)
file_browse_button.grid(row=1, column=1)
#----------------------------------------------------------------------
root.mainloop()

