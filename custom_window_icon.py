#---------------------------------------------
#     using custom window icon .ico file      
#---------------------------------------------

from tkinter import *

root = Tk()
root.geometry("300x200")
root.title("Custom Title Icon")

# you can set custom icons by using .ico files
# here we will chage the default icon using a custom .ico file present in database.
root.wm_iconbitmap(r"./imgs/gui_icon.ico")


#----------------------------------------------
root.mainloop()