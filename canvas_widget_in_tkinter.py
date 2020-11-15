#---------------------------
# Canvas widget in Tkinter  
#---------------------------

from tkinter import *

root = Tk()

canvas_width = 700
canvas_height = 500

root.geometry(f"{canvas_width}x{canvas_height}")
root.title(f"Canvas Widget with Tkinter")

# Making a canvas widget using the 'Canvas' class
can_widget = Canvas(root, width=canvas_width, height=canvas_height)

# packing the canvas widget
can_widget.pack()

# making a line using 'create_line' : """Create line with coordinates x1,y1,...,xn,yn."""
can_widget.create_line(0, 0, 10, 10, 10, 80, fill="red")

# making a rectangle using 'create_rectangle' : """Create rectangle with coordinates x1,y1,x2,y2."""
can_widget.create_rectangle(100,100, 500, 200, fill="blue")

# making an oval using 'create_oval' : """Create oval with coordinates x1,y1,x2,y2."""
can_widget.create_oval(100, 100, 500, 200, fill="red")
can_widget.create_oval(300, 300, 400, 400, fill="green")

# making text using 'create_text' : """Create text with coordinates x1,y1. as center coordinate"""
can_widget.create_text(100, 100, text='Jayant Yadav')

root.mainloop()