#--------------------------------
# Attributes of Label and Pack   
#--------------------------------

from tkinter import *

root = Tk()

root.geometry("700x500")

# Setting the title for the window :
root.title("This is the Window title !!...")

#-----------------------------------
# Some Important Label options :
# text : adds text
# bd : background
# fg : foreground
# font : sets the font
# padx : x padding 
# pady : y padding
# relief : border styling ... Types available : SUNKEN, RAISED, GROOVE, RIDGE
# underline : You can display an underline (_) below the nth letter of the text, counting from 0, by setting this option to n. The default is underline=-1, which means no underlining.

lbl1 = Label(text='''This is a long random test ...................
This is a long random test ...................
This is a long random test ...................
This is a long random test ...................
This is a long random test ...................
This is a long random test ...................
                  ''', bg="grey"   # seting the background as grey
                     , fg="white" # setting the foreground as white
                     , padx=50    # setting x padding
                     , pady=50    # setting y padding
                     , font=("comicsansms", 20, "italic") # setting the font and size, here it is passes as a tuple, however you can also specify it as a string :
                                                          # eg : font="comicsans 20 bold"
                     , borderwidth=5 # give a border width
                     , relief=SUNKEN # adding style to the border
                     , underline=1
             
             ) 

#------------------------------------------
# Some Important pack options :
# anchor : select nw, ne, sw,se (abbr for northwest, northeast, southwest and southeast respectively)
# side : top, bottom, left or right (by default this is set to 'top')
#        NOTE : If you specify anchor as 'sw' or 'se' without specifying the side, the container willstick to top as it is default.
# fill : The container will be filled (size proportional to the window stretch) in the x-axis
# padx :
# pady :

# lbl1.pack(anchor="sw", side=BOTTOM) # UNCOMMENT TO RUN

# lbl1.pack(side=BOTTOM, fill=X) # UNCOMMENT TO RUN : To fill in bottom X 

# we can also add padx and pady along with the usual attributes to give padding.
lbl1.pack(side=LEFT, fill=Y, padx=20, pady=20) # UNCOMMENT TO RUN : To fill in left Y 

root.mainloop()