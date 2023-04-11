import tkinter as tk
from tkinter import simpledialog

class UserSelectionScreen:
    
    def __init__(self, window, user_management):
        
        self.window = window
        self.user_management = user_management
        self.frame = tk.Frame(self.window, width=150, height=100)
        self.title_label = tk.Label(self.frame, text="Valitse käyttäjä")
        self.title_label.pack(pady=10)
        #self.users_frame = tk.Frame(self.frame)
        #self.users_frame.pack(pady=10)
        self.new_user_button = tk.Button(self.frame, text="New User", command=self.create_new_user, height=2, width=10, background="green")
        self.new_user_button.pack(side="left", padx=50)
        self.on_user_selected = None

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand= True)
        
    def hide(self):
        self.frame.pack_forget()

    def create_new_user(self):
        new_user_name = simpledialog.askstring("Uusi käyttäjä", "Syötä käyttäjän nimi:")
        if new_user_name:
            self.user_management.create_user(new_user_name, self.frame)
            
    def select_user(self, user):
        if self.on_user_selected:
            self.on_user_selected(user)
