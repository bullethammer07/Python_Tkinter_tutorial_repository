import tkinter as tk
from tkinter import Entry, Button, StringVar, filedialog


def on_entry_change(*args):
    # If entry content is not empty, enable the Submit button
    if entry_var.get().strip():
        submit_button.config(state="normal")
    else:
        submit_button.config(state="disabled")


def browse_file():
    file_path = filedialog.askopenfilename(title="Select a file")
    if file_path:
        entry_var.set(file_path)


def submit_file():
    file_path = entry_var.get().strip()
    print(f"File path submitted: {file_path}")


# Create the main window
root = tk.Tk()
root.title("File Submission")
root.geometry("400x100")

# Variable associated with the Entry widget
entry_var = StringVar()
entry_var.trace_add("write", on_entry_change)

# Create an Entry widget
entry = Entry(root, textvariable=entry_var, width=30)
entry.pack(side=tk.LEFT, padx=10, pady=10)

# Create a Browse button
browse_button = Button(root, text="Browse", command=browse_file)
browse_button.pack(side=tk.LEFT, padx=5)

# Create a Submit button, initially disabled
submit_button = Button(root, text="Submit", command=submit_file, state="disabled")
submit_button.pack(side=tk.LEFT, padx=5)

# Start the Tkinter event loop
root.mainloop()
