import tkinter as tk
from tkinter import messagebox

def show_popup():
    # Show a pop-up message box
    # messagebox.showinfo("Title", "This is a message.")
    op = messagebox.showerror("Title", "This is a message.")
    print(type(op))

# Create the main window
root = tk.Tk()
root.title("Pop-up Example")
root.geometry("200x100")

# Create a button that shows the pop-up
button = tk.Button(root, text="Show Pop-up", command=show_popup)
button.pack(padx=20, pady=20)

# Start the Tkinter event loop
root.mainloop()