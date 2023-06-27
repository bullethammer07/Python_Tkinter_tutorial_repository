# import tkinter as tk

# root = tk.Tk()
# root.title("Updated Frame scroll")
# root.geometry("500x200")

# frames = []

# def del_frame():
#     if frames:
#         pop = frames.pop()
#         pop.destroy()
#     print(len(frames))

# def create_frame():
#     fr=tk.Frame(root, borderwidth=2, bg="white", highlightbackground="green", highlightthickness=2)
#     fr.pack(sid=tk.TOP,fill="x")

#     b0 = tk.Button(fr, text="Add", command=create_frame).pack(side=tk.RIGHT)
#     b1 = tk.Button(fr, text="Remove", command=del_frame).pack(side=tk.RIGHT)

#     frames.append(fr)
#     print(len(frames))

# create_frame()

# root.mainloop()

#-----------------------------------------------------------------------

import tkinter as tk

root = tk.Tk()
root.title("Updated Frame scroll")
root.geometry("500x200")

frames = []

# Set the height of the containers and main window
container_height = 50
window_height = 500

# Create a canvas inside the main window
canvas = tk.Canvas(root, height=window_height)
canvas.pack(side="left", fill="both", expand=True)

# Create a scrollbar and attach it to the canvas
scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side="left", fill="y")
canvas.config(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold other frames
canvas_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

def del_frame():
    if frames:
        pop = frames.pop()
        pop.destroy()
    print(len(frames))

def create_frame(container):
    fr=tk.Frame(root, borderwidth=2, bg="white", highlightbackground="green", highlightthickness=2)
    fr.pack(sid=tk.TOP,fill="x")

    b0 = tk.Button(fr, text="Add", command=create_frame(container)).pack(side=tk.RIGHT)
    b1 = tk.Button(fr, text="Remove", command=del_frame).pack(side=tk.RIGHT)

    frames.append(fr)
    print(len(frames))

create_frame(canvas_frame)

# Update the scroll region after the main loop executed, to take initial frame into account
canvas.after(100, lambda: canvas.config(scrollregion=canvas.bbox("all")))

root.mainloop()