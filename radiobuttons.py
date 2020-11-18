#---------------------------
#       Radio Buttons       
#---------------------------

from tkinter import *

root = Tk()
root.geometry("700x500")
root.title("Radio Buttons")

#------------------------------------------
# making Radio buttons an Integer variable
#------------------------------------------
var = IntVar()
# giving a default value to var by setting it to 1
# var.set(1)

# making a radiobutton using 'Radiobutton'
# giving individual values to each
bt1 = Radiobutton(root, text="Option 1", variable=var, value=1).pack()
bt1 = Radiobutton(root, text="Option 2", variable=var, value=2).pack()
bt1 = Radiobutton(root, text="Option 3", variable=var, value=3).pack()
bt1 = Radiobutton(root, text="Option 4", variable=var, value=4).pack()

# Implementing a button to fetch the values of the Radiobuttos

def submit():
    print(f"Values submitted : {var.get()}")
    
Button(text="Submit", command=submit).pack()

#------------------------------------------
# making Radio buttons an String variable
#------------------------------------------
var2 = StringVar()
var2.set("x") # Initializing with a value

bt2 = Radiobutton(root, text="Option 1", variable=var2, value="opt1").pack()
bt2 = Radiobutton(root, text="Option 2", variable=var2, value="opt2").pack()
bt2 = Radiobutton(root, text="Option 3", variable=var2, value="opt3").pack()
bt2 = Radiobutton(root, text="Option 4", variable=var2, value="opt4").pack()


def submit2():
    print(f"Values submitted : {var2.get()}")

Button(text="Submit 2", command=submit2).pack()

#-----------------------------------
root.mainloop()