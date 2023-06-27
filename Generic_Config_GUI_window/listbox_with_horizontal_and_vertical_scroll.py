import tkinter as tk
from tkinter import Listbox, Scrollbar, Frame

# Function to populate the Listbox with sample data
def populate_listbox(listbox):
    # Adding shorter items
    for i in range(1, 11):
        listbox.insert(tk.END, f"Item {i}")
    
    # Adding a long item
    listbox.insert(tk.END, "This is a very long item that requires a horizontal scrollbar to be fully visible")

# Create main window
root = tk.Tk()
root.title("Listbox with Scrollbars")
root.geometry("350x250")

# Create a frame to hold the Listbox and Scrollbars
frame = Frame(root)
frame.pack(padx=10, pady=10)

# Create a vertical Scrollbar
v_scrollbar = Scrollbar(frame, orient=tk.VERTICAL)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a horizontal Scrollbar
h_scrollbar = Scrollbar(frame, orient=tk.HORIZONTAL)
h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Create a Listbox with fixed dimensions
listbox = Listbox(frame, yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set, height=10, width=30)
listbox.pack(side=tk.LEFT)

# Attach the Scrollbars to the Listbox
v_scrollbar.config(command=listbox.yview)
h_scrollbar.config(command=listbox.xview)

# Populate the Listbox with sample data
populate_listbox(listbox)

# Start the Tkinter event loop
root.mainloop()
