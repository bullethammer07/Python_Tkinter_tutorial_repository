import tkinter as tk
from tkinter import filedialog, Entry, Button, StringVar


def browse_file():
    # Open file dialog to select a file
    file_path = filedialog.askopenfilename()
    # Update the entry widget with the selected file path
    file_path_var.set(file_path)


def submit_file():
    # Get the file path from the entry widget
    file_path = file_path_var.get()
    
    # Try to open and read the file, and print its contents to the console
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("Contents of the file:")
            print(content)
    except Exception as e:
        print(f"An error occurred: {e}")


def update_submit_button(*args):
    # Enable the "Submit" button if there is text in the entry widget, otherwise disable it
    if file_path_var.get():
        submit_button.config(state='normal')
    else:
        submit_button.config(state='disabled')


# Create main window
root = tk.Tk()
root.title("File Browser")

# StringVar to hold the file path
file_path_var = StringVar()
# Monitor changes to the file path
file_path_var.trace_add("write", update_submit_button)

# Create an entry widget to display the file path
entry = Entry(root, textvariable=file_path_var, width=50)
entry.pack(padx=20, pady=20)

# Add "Browse" button to open the file dialog
browse_button = Button(root, text="Browse", command=browse_file)
browse_button.pack(side='left', padx=(20, 10), pady=20)

# Add "Submit" button to submit the file
submit_button = Button(root, text="Submit", command=submit_file, state='disabled')
submit_button.pack(side='right', padx=(10, 20), pady=20)

# Start the Tkinter event loop
root.mainloop()
