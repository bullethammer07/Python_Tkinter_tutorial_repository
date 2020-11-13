#---------------------------------------------
#     Displaying Images Using Label           
#---------------------------------------------

from tkinter import *

# NOTE : The PhotoImage class can read GIF and PGM/PPM images from files:
#        If you need to work with other file formats, the Python Imaging Library (PIL) contains classes 
#        that lets you load images in over 30 formats, and convert them to Tkinter-compatible image objects.

# FOR NOW STICK TO PNG FORMATS

# or you can install 'pillow' using pip install pillow to get PIL.
# now you can import Image and ImageTk from PIL :
from PIL import Image, ImageTk

root = Tk()

# giving basic geometry
root.geometry("691x732")

# making an image object using 'PhotoImage'
# pic1 = PhotoImage(file="rick.png") # 691x732

#-----------------------------------------------------------
# Code in between the lines is for JPEG Files
# uncomment above line and comment this block to use as PNG

jpg_image = Image.open("rick.jpg")
pic1 = ImageTk.PhotoImage(jpg_image)

#-----------------------------------------------------------

# now we have to put the image as a label
lbl1 = Label(image=pic1)

# packing the label
lbl1.pack()

root.mainloop()