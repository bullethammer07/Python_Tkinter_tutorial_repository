import tkinter as tk
from tkinter import Button, Entry, StringVar


def enable_widget():
    # Get widget ID from entry
    widget_id = entry_var.get().strip()
    
    # Get widget by ID
    widget = root.nametowidget(widget_id)
    
    # Enable the widget
    widget.config(state='normal')


def disable_widget():
    # Get widget ID from entry
    widget_id = entry_var.get().strip()
    
    # Get widget by ID
    widget = root.nametowidget(widget_id)
    
    # Disable the widget
    widget.config(state='disabled')


# Create the main window
root = tk.Tk()
root.title("Enable/Disable Widgets by ID")
root.geometry("300x200")

# Create an Entry to enter widget ID
entry_var = StringVar()
entry = Entry(root, textvariable=entry_var, width=20)
entry.pack(padx=10, pady=10)

# Create two buttons
button1 = Button(root, text="Button 1", width=10)
button1.pack(padx=10, pady=5)

button2 = Button(root, text="Button 2", width=10)
button2.pack(padx=10, pady=5)

# Create "Enable" and "Disable" buttons to change the state of widgets by ID
enable_button = Button(root, text="Enable", command=enable_widget, width=10)
enable_button.pack(side='left', padx=10, pady=10)

disable_button = Button(root, text="Disable", command=disable_widget, width=10)
disable_button.pack(side='right', padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
