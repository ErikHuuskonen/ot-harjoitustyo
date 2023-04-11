import tkinter as tk
from tkinter import simpledialog

class FolderSelectionScreen(tk.Frame):

    def __init__(self, window):
        super().__init__(window)
        self.window = window
        self.top = None  
        self.folders = []
        self.user = None
        
        self.new_folder_button = tk.Button(self, text="New Folder", command=self.new_folder)
        self.new_folder_button.pack(side="left", padx=5, pady=5)

    def show(self, user):
        self.user = user
        self.pack(fill=tk.BOTH, expand=True)
        self.update_folder_list()

    def hide(self):
        self.pack_forget()

    def create_new_folder(self):
        new_folder_name = simpledialog.askstring("Uusi tila", "Syötä tilan nimi:")
        if new_folder_name:
            self.create_folder(new_folder_name, self)
            self.update_folder_list()

    def update_folder_list(self):
        print(f"Updating folder list for user: {self.user}")  
        for widget in self.winfo_children():
            if isinstance(widget, tk.Button) and widget != self.new_folder_button:
                widget.destroy()

        for folder in self.folders:
            print(f"Adding folder button: {folder}")  
            folder_button = tk.Button(self, text=folder, command=lambda f=folder: self.folder_button_pressed(f))
            folder_button.pack(side="left", padx=5, pady=5)

    def create_folder(self, folder_name, frame):
        new_button = tk.Button(frame, text=folder_name, command=self.folder_button_pressed, height=2, width=10, background="green")
        new_button.pack(side="left", padx=5, pady=5)

        if folder_name not in self.folders:
            self.folders.append(folder_name)
    
    def set_user(self, user):
        self.current_user = user

    def folder_button_pressed(self, folder_name): #mene tiedostoon mindmap näkymään. 
        print(f"Folder selected: {folder_name}")


    def new_folder(self):
        folder_name = simpledialog.askstring("New Folder", "Enter folder name:")
        if folder_name and folder_name.strip():
            self.folders.append(folder_name.strip())
            self.update_folder_list()