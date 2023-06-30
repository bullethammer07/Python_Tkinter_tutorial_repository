import tkinter as tk
from tkinter import Canvas, Frame, Button, Scrollbar


class CollapsibleFrame(tk.Frame):
    def __init__(self, parent, text, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.toggle_button = Button(self, text=text, command=self.toggle)
        self.toggle_button.pack(fill='x', expand=True)
        
        self.sub_frame = Frame(self, highlightbackground="red", highlightthickness=1)
        
        # Initially the frame is collapsed
        self.is_expanded = False

    def toggle(self):
        if self.is_expanded:
            # Collapse
            self.sub_frame.pack_forget()
        else:
            # Expand
            self.sub_frame.pack(fill='x', expand=True)
        
        # Toggle the state
        self.is_expanded = not self.is_expanded
        
        # Update the scrollbar
        self.master.update_scrollbar()

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Collapsible Frames with Scrollbar")
        self.geometry("400x300")
        
        # Create the canvas
        self.canvas = Canvas(self)
        self.canvas.pack(side="left", fill="both", expand=True)
        
        # Create scrollbar
        self.scrollbar = Scrollbar(self, command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        # Create frame inside canvas
        self.main_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.main_frame, anchor="n")
        
        # Add collapsible frames
        for i in range(5):
            frame = CollapsibleFrame(self.main_frame, text=f"Frame {i+1}")
            frame.pack(fill='x', padx=10, pady=5)
            
            # Adding sample content to collapsible frames
            for j in range(3):
                tk.Label(frame.sub_frame, text=f"Content {j+1}").pack()

        # Update the scrollbar initially
        self.update_scrollbar()

    def update_scrollbar(self):
        self.main_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
