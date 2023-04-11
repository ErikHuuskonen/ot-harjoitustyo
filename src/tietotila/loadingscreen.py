import tkinter as tk
import os
import sys
from PIL import Image, ImageTk

class LoadingScreen:
    def __init__(self, window):
        self.window = window
        self.frame = tk.Frame(self.window)

        #set image
        image = Image.open("/Users/erikstandard/Desktop/ot-harjoitustyo/resources/tietotila_startingscreen.gif")

        # Convert the image to a format that can be displayed in a tkinter GUI
        photo = ImageTk.PhotoImage(image)

        # Create a label to display the image
        self.image_label = tk.Label(self.frame, image=photo)
        self.image_label.image = photo  # Save a reference to the photo to prevent garbage collection
        self.image_label.pack(pady=10)
    

        self.loading_label = tk.Label(self.frame, text="Loading Screen")
        self.loading_label.pack(pady=10)
        self.on_exit = None
        self.exit_button = tk.Button(self.frame, text="Continue", command= self.exit, fg="black")
        self.exit_button.place(x=100, y=100)
        self.exit_button.pack(pady=10)
        
        self.window.after(5000, self.exit)

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.frame.pack_forget()
    
    def exit(self):
        if self.on_exit:
            self.on_exit()
    
    def get_path(self):
        pass
