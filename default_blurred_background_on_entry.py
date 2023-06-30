import tkinter as tk

def on_entry_click(event):
    # function that gets called whenever entry is clicked
    if entry.get() == 'Enter text...':
       entry.delete(0, "end") # delete all the text in the entry
       entry.insert(0, '') # Insert blank for user input
       entry.config(fg = 'black')

def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Enter text...')
        entry.config(fg = 'grey')

# Create the main window
root = tk.Tk()
root.title("Entry with Placeholder Text")

# Create an Entry widget
entry = tk.Entry(root, fg='grey')
entry.pack(padx=10, pady=10)

# Set placeholder text
entry.insert(0, 'Enter text...')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)

# Start the main loop
root.mainloop()
