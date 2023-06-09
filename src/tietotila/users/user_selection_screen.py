"""
Käytetään käyttäjien luomiseen ja hallintaan.
"""
import tkinter as tk
from tkinter import simpledialog


class UserSelectionScreen:
    """
    Käytetään käyttäjän valintanäkymän luomiseen ja hallintaan.
    """

    def __init__(self, window, user_management, history: dict):
        """
        Alustaa ikkunan, käyttäjähallinnan, kehyksen, otsikon ja "New User" -painikkeen. 
        Asettaa käyttäjän valitsemisen käsittelijän arvoksi None.

        Args:
            window: Toplevel-ikkunan isäntäwidget.
            user_management: Käyttäjänhallintaluokan instanssi.
            history: Sanakirja, joka sisältää käyttäjien historian tiedot.
        """
        self.window = window
        self.user_management = user_management
        self.frame = tk.Frame(self.window, width=150, height=100)
        self.title_label = tk.Label(self.frame, text="Valitse käyttäjä")
        self.title_label.pack(pady=10)
        self.new_user_button = tk.Button(
            self.frame, text="New User", command=self.create_new_user, height=2, width=10, background="green")
        self.new_user_button.pack(side="left", padx=50)
        self.on_user_selected = None
        self.history = history

    def show(self):
        """
        Näyttää kehyksen.
        """
        self.frame.pack(fill=tk.BOTH, expand=True)
        for key in self.history:
            self.user_management.create_user(key, self.frame)

    def hide(self):
        """
        Piilottaa kehyksen.
        """
        self.frame.pack_forget()

    def create_new_user(self):
        """
         Luo uuden käyttäjän kysymällä käyttäjältä nimeä ja kutsuu user_management.create_user() -metodia.
        """
        new_user_name = simpledialog.askstring(
            "Uusi käyttäjä", "Syötä käyttäjän nimi:")
        if new_user_name:
            self.user_management.create_user(new_user_name, self.frame)

    def select_user(self, user):
        """
        Valitsee käyttäjän kutsuen on_user_selected-käsittelijää, jos se on määritelty.

        Args:
            user: Merkkijono, joka kuvaa valittua käyttäjää.
        """
        if callable(self.on_user_selected):
            # pylint: disable=not-callable
            self.on_user_selected(user)
