#----------------------------------
#    Radio Buttons with Image      
#----------------------------------

from tkinter import *

root = Tk()
root.geometry("150x50")

on_img = PhotoImage(file=r"./../imgs/button_on_state_small.png")
off_img = PhotoImage(file=r"./../imgs/button_off_state_small.png")

def click_beh(evt):
    # print(toggle_btn.config())
    foo = root.call(toggle_btn.cget('image'), 'cget', '-file')
    # print(foo)
    if foo == "./../imgs/button_on_state_small.png":
        # print("Button was ON ... setting it to off")
        toggle_btn.configure(image=off_img)
    else:
        # print("Button was OFF ... setting it to ON")
        toggle_btn.configure(image=on_img)
        
toggle_btn = Label(image=on_img)
toggle_btn.bind("<Button-1>", func=click_beh)
toggle_btn.pack()

#------------------------------------------------------------------------
root.mainloop()