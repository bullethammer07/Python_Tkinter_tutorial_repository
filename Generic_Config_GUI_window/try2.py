# Adds frame on a canvas which are part of the root.
# --> Creates a 'canvas' in root.
# --> Creates a 'scrollbar' in root
# --> All new frames are added to the canvas.

import tkinter as tk

# Function to add a new frame inside the canvas
def add_frame(container):
    frame = tk.Frame(container, bg='white', highlightbackground="red", highlightthickness=2)
    frame.pack(side=tk.TOP, fill="x")

    # Add buttons to the new frame
    add_button = tk.Button(frame, text="Add", command=lambda: add_frame(container))
    add_button.pack(side=tk.RIGHT)

    delete_button = tk.Button(frame, text="Delete", command=lambda: delete_frame(frame))
    delete_button.pack(side=tk.RIGHT)

    lbl = tk.Label(frame, text="This is some random text !!...",pady=0)
    lbl.pack(side=tk.TOP, fill="x", expand=True)

    # Update the scroll region as new frames are added
    canvas.config(scrollregion=canvas.bbox("all"))

# Function to delete a frame
def delete_frame(frame):
    frame.destroy()
    # Update the scroll region after deleting a frame
    canvas.config(scrollregion=canvas.bbox("all"))

# Create the main window
root = tk.Tk()
root.title("Red Bordered Frames with Scrollbar")

# Set the height of the containers and main window
window_height = 300

# Create a canvas inside the main window
canvas = tk.Canvas(root, height=window_height, highlightbackground="green", highlightthickness=2)
canvas.pack(side="left", fill="both", expand=True)

# Create a scrollbar and attach it to the canvas
scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side="left", fill="y")
canvas.config(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold other frames
canvas_frame = tk.Frame(canvas, highlightbackground="blue", highlightthickness=2)
# canvas_frame.pack(side=tk.TOP, fill="x")
canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

# Create the initial frame with a red border
add_frame(canvas_frame)

# Update the scroll region after the main loop executed, to take initial frame into account
canvas.after(100, lambda: canvas.config(scrollregion=canvas.bbox("all")))

# Run the Tkinter event loop
root.mainloop()