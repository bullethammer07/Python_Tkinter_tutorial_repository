import tkinter as tk
from tkinter import Frame, Button, Scrollbar, Canvas

# Function to add frames to the canvas
def add_frame():
    frame = Frame(canvas, bg='blue', height=50, width=200)
    frame.pack()
    update_scrollregion()

# Function to remove frames from the canvas
def remove_frame():
    if canvas.winfo_children():
        canvas.winfo_children()[-1].destroy()
        update_scrollregion()

# Function to update the scrollregion of the canvas
def update_scrollregion():
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox('all'))

# Create main window
root = tk.Tk()
root.geometry('250x300')

# Create a canvas
canvas = Canvas(root, bg='white')
canvas.pack(side='left', fill='both', expand=True)

# Add scrollbar to the canvas
scrollbar = Scrollbar(root, command=canvas.yview)
scrollbar.pack(side='right', fill='y')

canvas.config(yscrollcommand=scrollbar.set)

# Add "Add" and "Remove" buttons
add_button = Button(root, text='Add Frame', command=add_frame)
add_button.pack(pady=(20, 0))

remove_button = Button(root, text='Remove Frame', command=remove_frame)
remove_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
