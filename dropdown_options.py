import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Dropdown Menu")

# Define the options
options = ["Option 1", "Option 2"]

# Create a Tkinter variable
selected_option = tk.StringVar()
selected_option.set(options[0])  # set the default option

# Create the OptionMenu widget
dropdown = tk.OptionMenu(root, selected_option, *options)
dropdown.pack(padx=10, pady=10)

# Function to print selected option
def print_option():
    print(f"Selected option: {selected_option.get()}")

# Button to print selected option
button = tk.Button(root, text="Print Selected Option", command=print_option)
button.pack(padx=10, pady=10)

# Start the main loop
root.mainloop()
