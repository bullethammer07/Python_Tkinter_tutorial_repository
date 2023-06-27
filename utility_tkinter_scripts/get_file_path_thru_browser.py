import tkinter as tk
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename()
    entry_var.set(file_path)

def submit():
    file_path = entry_var.get()
    print("Selected File Path:", file_path)

window = tk.Tk()

entry_var = tk.StringVar()
entry = tk.Entry(window, textvariable=entry_var, width=50)
entry.pack(pady=10)

browse_button = tk.Button(window, text="Browse", command=browse_file)
browse_button.pack(side=tk.LEFT, padx=5, pady=5)

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack(side=tk.LEFT, padx=5, pady=5)

window.mainloop()
