"""
Käytetään graafisen käyttöliittymän rakentamiseen.
"""
import tkinter as tk
import os
from userselectionscreen import UserSelectionScreen

# lisäsin tämän management luokan perimään ui moduulin
class UserManagement(UserSelectionScreen):
    """
    UserManagement käsittelee käyttäjien luomista ja hallintaa.
    """

    def __init__(self, window, folder_selection_screen, user_selected_callback):
        """
        Alustaa käyttäjien listan, ikkunan, kansioiden valintanäkymän ja käyttäjän valitsemisen käsittelijän.
        """
        self.users = []
        self.window = window
        self.folder_selection_screen = folder_selection_screen
        self.user_selected_callback = user_selected_callback

    def create_user(self, user_name, frame):
        """
        Luo uuden käyttäjän ja lisää sille painikkeen käyttöliittymään. Lisää uuden käyttäjän käyttäjien listaan, jos sitä ei ole jo olemassa.
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
        """
        if self.user_selected_callback:
            self.user_selected_callback(user_name)

    def create_new_folder_in_history(self, folder_name):
        """
        Luo uuden kansion 'history' kansion sisälle annetulla nimellä.
        """
        current_file_path = os.path.dirname(os.path.abspath(__file__))
        history_path = os.path.join(current_file_path, "..", "history")
        new_folder_path = os.path.join(history_path, folder_name)
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
            print(f"Kansio luotu: {new_folder_path}")
        else:
            print(f"Kansio on jo olemassa: {new_folder_path}")
