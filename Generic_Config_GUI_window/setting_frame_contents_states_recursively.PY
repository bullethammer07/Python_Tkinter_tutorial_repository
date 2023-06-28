import tkinter as tk
from tkinter import Frame, Button, Label, OptionMenu, StringVar, Entry


def recursively_set_state(parent_widget, state):
    # Recursively set state of widget and its children
    for child in parent_widget.winfo_children():
        if child.winfo_children():
            recursively_set_state(child, state)

        try:
            child.configure(state=state)
        except tk.TclError:
            pass  # Not all widgets have a 'state' property, ignore those


def apply_state():
    selected_state = state_var.get().lower()
    if selected_state == "active":
        new_state = "normal"
    else:
        new_state = "disabled"
    recursively_set_state(frame1, new_state)


# Create the main window
root = tk.Tk()
root.title("Recursive State Setter")
root.geometry("350x300")

# Create a dropdown to select state
state_var = StringVar()
state_var.set("Active")
state_menu = OptionMenu(root, state_var, "Active", "Disabled")
state_menu.pack(pady=10)

# Button to apply state to child components of frame1
apply_button = Button(root, text="Apply to Frame 1", command=apply_state)
apply_button.pack()

# Frame 1
frame1 = Frame(root, bg="lightblue", padx=10, pady=10)
frame1.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Widgets inside Frame 1
button1 = Button(frame1, text="Button 1")
button1.pack()
entry1 = Entry(frame1)
entry1.pack()

# Frame 2
frame2 = Frame(root, bg="lightgreen", padx=10, pady=10)
frame2.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Widgets inside Frame 2
button2 = Button(frame2, text="Button 2")
button2.pack()
entry2 = Entry(frame2)
entry2.pack()

# Start the Tkinter event loop
root.mainloop()
