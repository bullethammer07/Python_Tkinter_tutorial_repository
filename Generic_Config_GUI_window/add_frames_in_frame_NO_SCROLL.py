# Simple frame adding in root
# --> Keeps on adding frames and increases the height of the window continuously.
# --> Window can even overflow entire monitor
# --> This needs a scrollbar

import tkinter as tk

# Function to add a new frame
def add_frame(container):
    frame = tk.Frame(container, height=container_height, bg='white',
                     highlightbackground="red", highlightthickness=2)
    frame.pack(side="top", fill="x")

    # Add buttons to the new frame
    add_button = tk.Button(frame, text="Add", command=lambda: add_frame(container))
    add_button.pack(side="left")

    delete_button = tk.Button(frame, text="Delete", command=lambda: delete_frame(frame))
    delete_button.pack(side="left")

# Function to delete a frame
def delete_frame(frame):
    frame.destroy()


# Create the main window
root = tk.Tk()
root.title("Red Bordered Frames")

# Set the height of the containers
container_height = 200

# Create the main container
main_container = tk.Frame(root)
main_container.pack(side="top", fill="both", expand=True)

# Create the initial frame with a red border
add_frame(main_container)

# Run the Tkinter event loop
root.mainloop()
