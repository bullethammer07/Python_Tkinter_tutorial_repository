# -------------------------------------------------
#   Grid Layout and Entry widgets and CheckButtons 
# -------------------------------------------------

# One way to pack objects is using pack(), another way to pack objects is using grid()
# grid can be used by specifying 'row' and 'column'
# by default row and column are 0,0 for every object

from tkinter import *

root = Tk()
root.geometry("400x100")

# creating two labels
l1 = Label(root, text="Username : ")
l2 = Label(root, text="Password  : ")
l3 = Label(root, text="Would you like to subscribe to our newsletter ? : ")

# packing l1 and l2 using grid
l1.grid()
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)

# Entry Widget : An Entry Widget is a widget through which you can input a value from the GUI

# Tkinter has four types of avariable classes :
#   BooleanVar
#   DoubleVar
#   IntVar
#   StringVar

# Making StringVar for two variables :
username_value = StringVar()
password_value = StringVar()
# Making IntVar for one variable :
subs_value = IntVar()

# making the entry widgets
usrname_entry = Entry(root, textvariable=username_value)
# to hide the character in password field we will display each letter as '*' using 'show'
pwd_entry = Entry(root, textvariable=password_value, show="*")
# Making a checkbutton 
subs_entry = Checkbutton(text="Yes/No", variable=subs_value)

# packing the above two entries using grid
usrname_entry.grid(row=0, column=1)
pwd_entry.grid(row=1, column=1)
subs_entry.grid(row=2, column=1)

# Making a function to get the value of the username and password
def get_val():
    # getting the username and password values
    uname = username_value.get()
    pwd = password_value.get()
    nletter = subs_value.get()

    print(f"Username entered is : {uname}")
    print(f"Password entered is : {pwd}")
    print(f"Newsletter Choice   : {nletter}")

# making a button that can be used to get the values
# NOTE : button here is implemented as a one-line

Button(text="Sign In", command=get_val).grid(row=3)

root.mainloop()