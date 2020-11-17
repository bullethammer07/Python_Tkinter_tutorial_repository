#---------------------------------
# Browse or Input  a Directory    
#---------------------------------

from tkinter import *

root = Tk()
root.title("Browsing or Input a Directory")
root.geometry("700x500")

dir_image = PhotoImage(file=r"d:/icons pack/icons/directory_icon.png")
# NOTE : here we have used 'subsample' to make the png img small in size for icon.
#        specifying a parameter of 1 will give original size, increasing from 1 will reduce the image size.
small_dir_image = dir_image.subsample(25)
# To put image to the left of the button we have used 'compund=LEFT'
browse_button = Button(root, text="Select Folder", image=small_dir_image, compound=LEFT, width=100, height=20)
browse_button.grid(row=0, column=0)
#----------------------------------------------------------------------
root.mainloop()

