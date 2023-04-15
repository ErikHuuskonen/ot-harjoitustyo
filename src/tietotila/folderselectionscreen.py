"""
Tässä moduulissa on FolderSelectionScreen-luokka, joka luo ikkunan kansiovalintaa varten. 
Luokka sisältää metodit uuden kansion luomiseen, kansion listaamiseen, piilottamiseen, käyttäjän asettamiseen ja kansion valitsemiseen. 
Moduuli käyttää tkinter-kirjastoa ikkunan luomiseen ja simpledialog-kirjastoa kansion nimen kysymiseen.
"""
import tkinter as tk
from tkinter import simpledialog
class FolderSelectionScreen(tk.Frame):
    """
    Luokka kansion valintaikkunaa varten
    """
    def __init__(self, window, on_mindmap_selected=None):
        """
        Alustaa FolderSelectionScreen-luokan annetulla ikkunalla ja on_mindmap_selected-kutsulla
        """
        super().__init__(window)
        self.window = window
        self.top = None
        self.folders = []
        self.current_user = None
        self.user = None
        self.on_mindmap_selected = on_mindmap_selected
        self.new_folder_button = tk.Button(self, text="New Folder", command=self.new_folder)
        self.new_folder_button.pack(side="left", padx=5, pady=5)
    def show(self, user):
        """
        Näyttää FolderSelectionScreenin annetulla käyttäjällä
        """
        self.user = user
        self.pack(fill=tk.BOTH, expand=True)
        self.update_folder_list()
    def hide(self):
        """
        Piilottaa FolderSelectionScreenin
        """
        self.pack_forget()
    def create_new_folder(self):
        """
        Luo uuden kansion annetulla nimellä ja päivittää kansion listan
        """
        new_folder_name = simpledialog.askstring("Uusi tila", "Syötä tilan nimi:")
        if new_folder_name:
            self.create_folder(new_folder_name, self)
            self.update_folder_list()
    def update_folder_list(self):
        """
        Päivittää kansion listan nykyisillä kansioilla ja tuhoaa aikaisemmat kansion painikkeet
        """
        print(f"Updating folder list for user: {self.user}")
        for widget in self.winfo_children():
            if isinstance(widget, tk.Button) and widget != self.new_folder_button:
                widget.destroy()
        for folder in self.folders:
            print(f"Adding folder button: {folder}")
            folder_button = tk.Button(self, text=folder, command=lambda f=folder: self.folder_button_pressed(f))
            folder_button.pack(side="left", padx=5, pady=5)
    def create_folder(self, folder_name, frame):
        """
        Luo uuden kansion annetulla nimellä annetussa kehyksessä
        """
        new_button = tk.Button(frame, text=folder_name, command=lambda: self.folder_button_pressed(folder_name), height=2, width=10, background="green")
        new_button.pack(side="left", padx=5, pady=5)
        if folder_name not in self.folders:
            self.folders.append(folder_name)
    def set_user(self, user):
        """
        set user
        """
        self.current_user = user
    def folder_button_pressed(self, folder_name):
        """
        Käsittelee kansion painikkeen painalluksen ja kutsuu on_mindmap_selected-kutsua
        """
        print(f"Folder selected: {folder_name}")
        if self.on_mindmap_selected:
            self.on_mindmap_selected()
    def new_folder(self):
        """
        Luo uuden kansion annetulla nimellä ja päivittää kansion listan
        """
        folder_name = simpledialog.askstring("New Folder", "Enter folder name:")
        if folder_name and folder_name.strip():
            self.folders.append(folder_name.strip())
            self.update_folder_list()
    