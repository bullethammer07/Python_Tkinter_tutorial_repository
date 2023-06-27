# # This code can be used for creation of a generic widnow for various GUI based purposes

# import tkinter as tk

# window_title = "Window Title"

# # Create he main window
# root = tk.Tk()
# root.title(window_title)
# x_wd="800"
# y_wd="500"
# glbl_ft_size=8 # Global font size
# root.geometry(f"{x_wd}x{y_wd}")
# root.resizable(0,1) # Window resizeable only in y direction

# # Create a canvas and a scrollbar
# canvas = tk.Canvas(root)
# scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
# scrollable_frame = tk.Frame(canvas)

# # Make the frame a scrollable region of the canvas
# canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
# canvas.configure(yscrollcommand=scrollbar.set)

# # Pack the canvas and the scrollbar into the window
# canvas.pack(side="left", fill="both", expand=True)
# scrollbar.pack(side="right", fill="y")

# container_height=200
# container = tk.Frame(scrollable_frame, height=container_height, bg='white', highlightbackground="red", highlightthickness=2)
# # Make the frame span across the y-axis
# container.pack(side="top", fill="x")

# # mainloop
# root.mainloop()

# #---------------------------------------------------------------------------------------------------------------------------------------------
# import tkinter as tk

# # Function to add a new frame
# def add_frame():
#     new_frame = tk.Frame(root, height=container_height, bg='white',
#                          highlightbackground="red", highlightthickness=2)
#     new_frame.pack(side="top", fill="x")


# # Create the main window
# root = tk.Tk()
# root.title("Red Bordered Containers")

# # Set the height of the containers
# container_height = 200

# # Create the initial frame with a red border
# initial_frame = tk.Frame(root, height=container_height, bg='white',
#                          highlightbackground="red", highlightthickness=2)
# initial_frame.pack(side="top", fill="x")

# # Add a button to the initial frame to add more frames
# add_button = tk.Button(initial_frame, text="Add Frame", command=add_frame)
# add_button.pack()

# # Run the Tkinter event loop
# root.mainloop()

# #---------------------------------------------------------------------------------------------------------------------------------------------

import tkinter as tk

# Function to add a new frame inside the canvas
def add_frame():
    frame = tk.Frame(canvas, height=container_height, bg='white',
                     highlightbackground="red", highlightthickness=2)
    frame.pack(side="top", fill="x")

    # Update the scroll region as new frames are added
    canvas.config(scrollregion=canvas.bbox("all"))


# Create the main window
root = tk.Tk()
root.title("Red Bordered Containers")

# Set the height of the containers and main window
container_height = 200
window_height = 500

# Create a canvas inside the main window
canvas = tk.Canvas(root, height=window_height)
canvas.pack(side="left", fill="both", expand=True)

# Create a scrollbar and attach it to the canvas
scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side="left", fill="y")
canvas.config(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold other frames
canvas_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

# Create the initial frame with a red border
initial_frame = tk.Frame(canvas_frame, height=container_height, bg='white',
                         highlightbackground="red", highlightthickness=2)
initial_frame.pack(side="top", fill="x")

# Add a button to the initial frame to add more frames
add_button = tk.Button(initial_frame, text="Add Frame", command=add_frame)
add_button.pack()

# Update the scroll region after the main loop executed, to take initial frame into account
canvas.after(100, lambda: canvas.config(scrollregion=canvas.bbox("all")))

# Run the Tkinter event loop
root.mainloop()
