import tkinter as tk
from tkinter import Text, Scrollbar, Button

def add_text():
    text_widget.insert(tk.END, "Some more text\n")

# Create main window
root = tk.Tk()
root.title("Scrollbar Example")
root.geometry("300x200")

# Create a Scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a Text widget with attached scrollbar
text_widget = Text(root, wrap=tk.WORD, yscrollcommand=scrollbar.set)
text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Configure scrollbar to the text widget
scrollbar.config(command=text_widget.yview)

# Button to add text to text widget
add_text_button = Button(root, text="Add Text", command=add_text)
add_text_button.pack()

# Start the Tkinter event loop
root.mainloop()
