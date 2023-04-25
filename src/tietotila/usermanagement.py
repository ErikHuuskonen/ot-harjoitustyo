"""
Käytetään graafisen käyttöliittymän rakentamiseen.
"""
import tkinter as tk
import sys
if "tietotila" in sys.modules:
    from tietotila.folderselectionscreen import FolderSelectionScreen
else:
    from folderselectionscreen import FolderSelectionScreen
class UserManagement():
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
        new_button = tk.Button(frame, text=user_name, command=lambda: self.user_button_pressed(user_name), height=2, width=10, background="green")
        new_button.pack(side="left", padx=5, pady=5)
        if user_name not in self.users:
            self.users.append(user_name)
    def get_users(self):
        """
        Palauttaa käyttäjien listan.
        """
        return self.users
    def user_button_pressed(self, user_name):
        """
        Käsittelee käyttäjäpainikkeen painallusta. Tulostaa "painettu" ja kutsuu käyttäjän valitsemisen käsittelijää, jos sellainen on määritelty. Tulostaa käyttäjien listan.
        """
        print("painettu")
        if self.user_selected_callback:
            self.user_selected_callback(user_name)
            print(self.users)