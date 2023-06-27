import tkinter as tk
from tkinter import Toplevel, Entry, Label, Button, StringVar

# Function to fetch the data from the new window and update the main window
def submit_data(entry, string_var):
    data = entry.get()
    string_var.set(f"Data from new window: {data}")
    # Optionally close the new window after submission
    entry.master.destroy()

# Function to create a new window
def create_new_window(string_var):
    new_window = Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("800x500")
    
    # Create an input field
    entry = Entry(new_window)
    entry.pack(padx=20, pady=20)
    
    # Add a submit button that will fetch the data
    submit_button = Button(new_window, text="Submit", command=lambda: submit_data(entry, string_var))
    submit_button.pack()
    
# Create the main window
root = tk.Tk()
root.title("Main Window")

# StringVar to store and display data in the main window
data_string_var = StringVar()
data_string_var.set("Waiting for data...")

# Label to display data in the main window
data_label = Label(root, textvariable=data_string_var)
data_label.pack(padx=20, pady=20)

# Add a button that will open a new window
open_new_window_button = Button(root, text="Open New Window", command=lambda: create_new_window(data_string_var))
open_new_window_button.pack(padx=20, pady=20)

# Start the Tkinter event loop
root.mainloop()
