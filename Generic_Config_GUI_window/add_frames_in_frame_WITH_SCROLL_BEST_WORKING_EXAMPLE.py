import tkinter as tk
from tkinter import Frame, Button, Canvas, Scrollbar


class DynamicFramesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dynamic Frames")
        self.geometry("300x300")

        # Create a canvas inside the root window
        self.canvas = Canvas(self)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a scrollbar
        self.scrollbar = Scrollbar(self, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        # Configure the canvas to use the scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame inside the canvas to hold other frames
        self.inner_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # Update scrollregion as inner_frame changes
        self.inner_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Button to add frames
        self.add_frame_btn = Button(self, text="Add Frame", command=self.add_frame)
        self.add_frame_btn.pack()

    def add_frame(self):
        # Create a new frame
        frame = Frame(self.inner_frame, bd=2, relief="ridge", padx=10, pady=5)
        frame.pack(fill=tk.X, padx=5, pady=5)

        # Delete button inside the new frame
        delete_btn = Button(frame, text="Delete", command=lambda: self.delete_frame(frame))
        delete_btn.pack()

    def delete_frame(self, frame):
        frame.destroy()


if __name__ == "__main__":
    app = DynamicFramesApp()
    app.mainloop()
