# Code generated from ChatGPT

import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Frame creator")

# Function to add a frame
def add_frame():
    frame = tk.Frame(root, height=100, width=100, borderwidth=1, relief=tk.SUNKEN)
    frame.pack(pady=10)

# Create button to add frame
add_frame_button = tk.Button(root, text="Add frame", command=add_frame)
add_frame_button.pack()

# Start the application
root.mainloop()
