
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Project")

# Function to add a new frame inside the canvas
def add_frame(container):
    frame = tk.Frame(container, height=container_height, bg='white', highlightbackground="red", highlightthickness=2)
    frame.pack(side=tk.TOP, fill="x")

    content_frame = tk.Frame(frame, bg="white", highlightbackground="pink", highlightthickness=1) # Frame for content
    content_frame.pack(side=tk.TOP, fill="x")
    button_frame = tk.Frame(frame, bg="white", highlightbackground="pink", highlightthickness=1) # Frame for Buttons
    button_frame.pack(side=tk.BOTTOM, fill="x")

    print_label = tk.Label(frame, text="This is some random text !!...")
    print_label.pack(side=tk.LEFT)

    # Add buttons to the new frame
    add_button = tk.Button(button_frame, text="Add", command=lambda: add_frame(container))
    add_button.pack(side="right")

    delete_button = tk.Button(button_frame, text="Delete", command=lambda: delete_frame(frame))
    delete_button.pack(side="right")

    # Update the scroll region as new frames are added
    canvas.config(scrollregion=canvas.bbox("all"))

# Function to delete a frame
def delete_frame(frame):
    frame.destroy()
    # Update the scroll region after deleting a frame
    canvas.config(scrollregion=canvas.bbox("all"))

# Create a canvas inside the main window
container_height = 50
main_window_height = 500
canvas = tk.Canvas(root, height=main_window_height, highlightbackground="green", highlightthickness=2)
canvas.pack(side="left", fill="both", expand=True)

# Create a scrollbar and attach it to the canvas
scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side="left", fill="y")
canvas.config(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold other frames
initial_frame = tk.Frame(canvas, height=100, highlightbackground="black", highlightthickness=2).pack(fill="x", anchor="n")
# canvas.create_window((0, 0), window=initial_frame, anchor="nw")

add_frame(canvas) # Create the initial frame with a red border

# Update the scroll region after the main loop executed, to take initial frame into account
canvas.after(100, lambda: canvas.config(scrollregion=canvas.bbox("all")))

#---------------------------------------------------------------------------------------------------------------------------

# Run the Tkinter event loop
root.mainloop()