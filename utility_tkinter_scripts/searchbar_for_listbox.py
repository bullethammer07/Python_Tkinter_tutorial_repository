import tkinter as tk
from tkinter import Entry, Listbox, StringVar, Scrollbar, Button


def on_search_change(*args):
    # Get the search pattern
    search_pattern = search_var.get().lower()
    
    # Clear the listbox
    listbox.delete(0, tk.END)
    
    # Re-populate listbox with items that match the search pattern
    for item in all_items:
        if search_pattern in item.lower():
            listbox.insert(tk.END, item)


def submit_selection():
    # Get selected items from the listbox
    selected_indices = listbox.curselection()
    selected_items = [listbox.get(index) for index in selected_indices]
    
    # Print selected items to console
    print(f"Selected items: {selected_items}")


# Create the main window
root = tk.Tk()
root.title("ListBox Search and Selection")
root.geometry("300x350")

# Variable associated with the search Entry widget
search_var = StringVar()
search_var.trace_add("write", on_search_change)

# Create a search Entry widget
search_entry = Entry(root, textvariable=search_var, width=30)
search_entry.pack(padx=10, pady=10)

# Create a Listbox widget with multiple select mode
listbox = Listbox(root, width=40, height=10, selectmode=tk.MULTIPLE)
listbox.pack(padx=10, pady=5, expand=True, fill="both")

# Scrollbar for the listbox
scrollbar = Scrollbar(listbox, orient="vertical")
scrollbar.pack(side="right", fill="y")
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# All items (could come from file or database)
all_items = ["Apple", "Banana", "Cherry", "Orange", "Strawberry", "Grape", "Lemon", "Blueberry", "Raspberry"]

# Initially populate listbox with all items
for item in all_items:
    listbox.insert(tk.END, item)

# Create a Submit button to submit the selected items
submit_button = Button(root, text="Submit", command=submit_selection)
submit_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
