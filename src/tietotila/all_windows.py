import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class LoadingScreen:

    def __init__(self):
        pass
        

class MainWindow():
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)
        self.title = self.window.title('Tietotila')
        self.show_loading_screen()

    def show_loading_screen(self):
        pass

    def show_users(self):
        users_frame = ttk.Frame(master=self.window)
        users_frame.pack()

        button_new_user = ttk.Button(master=users_frame, text='New User')
        button_new_user.pack(pady=10)

        button_choose_user = ttk.Button(master=users_frame, text='Choose User')
        button_choose_user.pack(pady=10)

        
