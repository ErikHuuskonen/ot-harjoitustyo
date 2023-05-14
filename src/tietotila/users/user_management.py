"""
Käytetään graafisen käyttöliittymän rakentamiseen.
"""
import tkinter as tk
import os


class UserManagement():
    """
    UserManagement käsittelee käyttäjien luomista ja hallintaa.
    """

    def __init__(self, window, folder_selection_screen, user_selected_callback):
        """
        Alustaa käyttäjien listan, ikkunan, kansioiden valintanäkymän ja käyttäjän valitsemisen käsittelijän.

        Args:
            window: Toplevel-ikkunan isäntäwidget.
            folder_selection_screen: Kansion valintanäkymä.
            user_selected_callback: Funktio, joka kutsutaan, kun käyttäjä on valittu.
        """
        self.users = []
        self.window = window
        self.folder_selection_screen = folder_selection_screen
        self.user_selected_callback = user_selected_callback

    def create_user(self, user_name, frame):
        """
        Luo uuden käyttäjän ja lisää sille painikkeen käyttöliittymään. Lisää uuden käyttäjän käyttäjien listaan, jos sitä ei ole jo olemassa.

        Args:
            user_name: Merkkijono, joka kuvaa uuden käyttäjän nimeä.
            frame: Widget, johon uusi painike lisätään.
        """
        new_button = tk.Button(frame, text=user_name, command=lambda: self.user_button_pressed(
            user_name), height=2, width=10, background="green")
        new_button.pack(side="left", padx=5, pady=5)
        if user_name not in self.users:
            self.users.append(user_name)
            self.create_new_folder_in_history(user_name)

    def get_users(self):
        """
        Palauttaa käyttäjien listan.
        """
        return self.users

    def user_button_pressed(self, user_name):
        """
        Käsittelee käyttäjäpainikkeen painallusta. Tulostaa "painettu" 
        ja 
        kutsuu käyttäjän valitsemisen käsittelijää, jos sellainen on määritelty. Tulostaa käyttäjien listan.

        Args:
            user_name: Merkkijono, joka kuvaa painetun painikkeen nimen.
        """
        if self.user_selected_callback:
            self.user_selected_callback(user_name)

    def create_new_folder_in_history(self, folder_name):
        """
        Luo uuden kansion 'history' kansion sisälle annetulla nimellä.

        Args:
            folder_name: Merkkijono, joka kuvaa uuden kansion nimeä.
        """
        current_file_path = os.path.dirname(os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))))
        history_path = os.path.join(current_file_path, "history")
        new_folder_path = os.path.join(history_path, folder_name)
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
        else:
            pass
