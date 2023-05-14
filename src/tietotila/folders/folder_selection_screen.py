"""
Tässä moduulissa on FolderSelectionScreen-luokka, joka luo ikkunan kansiovalintaa varten. 
Luokka sisältää metodit uuden kansion luomiseen, kansion listaamiseen, piilottamiseen, 
käyttäjän asettamiseen ja kansion valitsemiseen. 
Moduuli käyttää tkinter-kirjastoa ikkunan luomiseen 
ja simpledialog-kirjastoa kansion nimen kysymiseen.
"""
import os
import tkinter as tk
from tkinter import simpledialog
from src.tietotila.folders.folder_management import FolderManagement


class FolderSelectionScreen(tk.Frame, FolderManagement):
    """
    Luokka kansion valintaikkunaa varten
    """

    def __init__(self, window, history: dict, on_mindmap_selected=None):
        """
        Alustaa FolderSelectionScreen-luokan annetulla ikkunalla ja on_mindmap_selected-kutsulla

        Args:
            window: 
                TKinter-elementti, joka toimii pääikkunana kansion valintaikkunalle.
            history: 
                Sanakirja, joka sisältää käyttäjän historian tiedot.
            on_mindmap_selected: 
                Kutsuttava arvo, jota kutsutaan, kun miellekartta on valittu. Oletusarvo on None.
        """
        super().__init__(window)
        self.window = window
        self.top = None
        self.folders = []
        self.current_user = None
        self.user = None
        self.folder_name = None
        self.on_mindmap_selected = on_mindmap_selected
        self.new_folder_button = tk.Button(
            self, text="Uusi miellekartta", command=self.new_folder)
        self.new_folder_button.pack(side="left", padx=5, pady=5)
        self.history = history

    def show(self, user):
        """
        Näyttää FolderSelectionScreenin annetulla käyttäjällä
        
        Args:
            user: 
                Käyttäjän nimi, jonka tiedot halutaan näyttää.
        """
        if user in self.history:
            lista = self.history[user]
            if len(lista) > 0:
                for name in lista:
                    self.create_folder(name, self)
        self.user = user
        self.pack(fill=tk.BOTH, expand=True)
        self.update_folder_list()

    def hide(self):
        """
        Piilottaa FolderSelectionScreenin
        """
        self.pack_forget()

    def update_folder_list(self):
        """
        Päivittää kansion listan nykyisillä kansioilla ja tuhoaa aikaisemmat kansion painikkeet
        """
        for widget in self.winfo_children():
            if isinstance(widget, tk.Button) and widget != self.new_folder_button:
                widget.destroy()
        for folder in self.folders:
            folder_button = tk.Button(
                self, text=folder, command=lambda f=folder: self.folder_button_pressed())
            folder_button.pack(side="left", padx=5, pady=5)

    def create_folder(self, folder_name, frame):
        """
        Luo uuden kansion annetulla nimellä annetussa kehyksessä

        Args:
            folder_name: 
                Merkkijono, joka kuvaa luotavan kansion nimeä.
            frame: 
                TKinter-elementti, johon uusi kansio luodaan.
        """
        new_button = tk.Button(frame, text=folder_name, command=self.folder_button_pressed, height=2, width=10, background="green")
        new_button.pack(side="left", padx=5, pady=5)
        if folder_name not in self.folders:
            self.folders.append(folder_name)

    def set_user(self, user):
        """
        Asettaa käyttäjän.

        Args:
            user: 
                Käyttäjän nimi, joka halutaan asettaa.
        """
        self.current_user = user

    def folder_button_pressed(self):
        """
        Käsittelee kansion painikkeen painalluksen ja kutsuu on_mindmap_selected-kutsua
        """
        if self.on_mindmap_selected and self.folder_name is not None:
            self.on_mindmap_selected()
        else:
            self.on_mindmap_selected()

    def new_folder(self):
        """
        Luo uuden kansion annetulla nimellä ja päivittää kansion listan
        """
        folder_name = simpledialog.askstring(
            "New Folder", "Enter folder name:")
        self.folder_name = folder_name
        if folder_name and folder_name.strip():
            self.folders.append(folder_name.strip())
            self.update_folder_list()
            current_file_path = os.path.abspath(__file__)
            current_file_path = os.path.dirname(os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))))
            user_folder = os.path.join(current_file_path, "history", self.user)
            empty_pickle_file_name = f"{folder_name.strip()}.pickle"
            self.create_empty_pickle_file(empty_pickle_file_name, user_folder)
