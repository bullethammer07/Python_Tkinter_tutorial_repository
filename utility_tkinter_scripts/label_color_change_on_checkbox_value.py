import tkinter as tk
from tkinter import Label, Checkbutton, IntVar


def on_checkbox_change(*args):
    # If checkbox is selected
    if checkbox_state.get():
        label.config(bg='green')
    # If checkbox is deselected
    else:
        label.config(bg='red')


# Create the main window
root = tk.Tk()
root.title("Label Color Toggle")
root.geometry("200x100")

# Variable associated with the Checkbox
checkbox_state = IntVar()
checkbox_state.trace_add("write", on_checkbox_change)

# Create a Label
label = Label(root, text="Color Toggle", bg='red', width=20, height=2)
label.pack(padx=10, pady=5)

# Create a Checkbox
checkbox = Checkbutton(root, text="Toggle Color", variable=checkbox_state)
checkbox.pack(padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()
