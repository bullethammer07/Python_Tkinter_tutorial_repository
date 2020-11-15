#-----------------------------------------------
# taking user input and storing in file
#-----------------------------------------------

from tkinter import *
import os

root = Tk()
root.geometry("220x120")

# creating two labels
l1 = Label(root, text="Name          : ")
l2 = Label(root, text="Age           : ")
l3 = Label(root, text="Mail ID       : ")
l4 = Label(root, text="If Non-Indian : ")

# packing l1 and l2 using grid
l1.grid()
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)
l4.grid(row=3, column=0)

# Making StringVar for two variables :
name_value = StringVar()
age_value = StringVar()
mail_value = StringVar()
# Making IntVar for one variable :
nation_value = IntVar()

# making the entry widgets
name_entry = Entry(root, textvariable=name_value)
age_entry = Entry(root, textvariable=age_value)
mail_entry = Entry(root, textvariable=mail_value)
nation_entry = Checkbutton(text="Yes/No", variable=nation_value)

# packing the above two entries using grid
name_entry.grid(row=0, column=1)
age_entry.grid(row=1, column=1)
mail_entry.grid(row=2, column=1)
nation_entry.grid(row=3, column=1)

# Making a function to get the value of the username and password
def get_val():
    # getting the username and password values
    name = name_value.get()
    age = age_value.get()
    mail = mail_value.get()
    nation = nation_value.get()

    # Making a file to store all the user data entered
    #  NOTE : Opening in append mode, as we would like a new entry to always be added below
    with open("records.txt", "a") as f:
    
        print("Logging specified data")    
        f.write(f"{name}, {age}, {mail}, {nation}" + "\n")
        
    f.close()

# making function for the 'Delete Log button'
def del_log():
    if os.path.exists("records.txt"):
        print("Deleting Records file ...")
        os.remove("records.txt")
    else:
        print("Records file does not exist !!....")

# making a button that can be used to get the values
# NOTE : button here is implemented as a one-line

Button(text="Submit", command=get_val).grid(row=4)
Button(text="Delete Log", command=del_log).grid(row=4, column=1)

root.mainloop()