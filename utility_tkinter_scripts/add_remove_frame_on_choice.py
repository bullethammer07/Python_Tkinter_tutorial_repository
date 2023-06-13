import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Interactive Frame Management")  
root.geometry("500x300")  

# Create a canvas and a scrollbar
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

# Make the frame a scrollable region of the canvas
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Update the scrollregion of the canvas every time its size changes
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)

# Pack the canvas and the scrollbar into the window
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# List to store all frames
frames = []

# Function to add a frame
def add_frame():
    frame = tk.Frame(scrollable_frame, height=100, width=100, borderwidth=1, relief=tk.SUNKEN)
    frame.pack(pady=10, fill="y")
    frames.append(frame)

# Function to remove the last frame added
def remove_frame():
    if frames:
        frame_to_remove = frames.pop()
        frame_to_remove.destroy()

# Create button to add frame
add_frame_button = tk.Button(root, text="Add frame", command=add_frame)
add_frame_button.pack()

# Create button to remove frame
remove_frame_button = tk.Button(root, text="Remove frame", command=remove_frame)
remove_frame_button.pack()

# Start the application
root.mainloop()
