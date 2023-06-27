import tkinter as tk
from tkinter import Listbox, Scrollbar

# Function to populate the Listbox with sample data
def populate_listbox(listbox):
    for i in range(1, 51):
        listbox.insert(tk.END, f"Item {i}")

# Create main window
root = tk.Tk()
root.title("Listbox with Scrollbar")
root.geometry("350x250")

# Create a frame to hold the Listbox and Scrollbar
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create a Scrollbar
scrollbar = Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a Listbox with fixed dimensions
listbox = Listbox(frame, yscrollcommand=scrollbar.set, height=10, width=30)
listbox.pack(side=tk.LEFT)

# Attach the Scrollbar to the Listbox
scrollbar.config(command=listbox.yview)

# Populate the Listbox with sample data
populate_listbox(listbox)

# Start the Tkinter event loop
root.mainloop()
