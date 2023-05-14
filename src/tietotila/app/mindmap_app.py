"""
Tämä muduuli luo käyttöliittymän mindmap-sovellukselle. 
Sovelluksessa käyttäjä voi luoda mindmap-näkymän, lisätä solmuja ja 
navigoida mindmapin eri osien välillä. 
Moduulissa käytetään tkinter-kirjastoa käyttöliittymän rakentamiseen, 
ja siinä on luokkia, jotka vastaavat eri näkymistä ja käyttöliittymän toiminnallisuuksista.
"""
import tkinter as tk
import os
import inspect
from src.tietotila.users.user_management import UserManagement
from src.tietotila.loading_screen.loading_screen import LoadingScreen
from src.tietotila.users.user_selection_screen import UserSelectionScreen
from src.tietotila.folders.folder_selection_screen import FolderSelectionScreen
from src.tietotila.mindmaps.mindmap_screen import MindMap


class MindmapApp():
    """
    Tämä luokka muodostaa mindmap sovelluksen 
    käyttämiseen tarvittavat moduulit ja luokat. 
    Se sisältää funktiot eri näkyminen välillä 
    siirtymiseen sekä kutsuu kunkin moduulin luokan konstruktoria.
    """

    def __init__(self):
        """
        Luokan rakentaja, joka luo Mindmapapp-objektin.
        """
        self.window = tk.Tk()
        self.window.geometry('1000x1200')
        self.window.title("Tietotila")
        self.history = self.get_user_files_dict()
        self.loading_screen = LoadingScreen(self.window)
        self.user_management = UserManagement(
            self.window, self.show_folder_selection_screen, self.show_folder_selection_screen)
        self.user_selection_screen = UserSelectionScreen(
            self.window, self.user_management, self.history)
        self.folder_selection_screen = FolderSelectionScreen(
            self.window, self.history, self.show_mindmap_screen)
        self.user_management = UserManagement(
            self.window, self.folder_selection_screen, self.show_folder_selection_screen)
        self.mindmap_screen = MindMap(self.window)
        self.loading_screen.on_exit = self.show_user_selection_screen

    def run(self):
        """
        funktio jota kutsutaan kun ohejelma käynnistetään
        """
        self.show_loading_screen()
        self.window.mainloop()

    def show_loading_screen(self):
        """
        funktio joka näyttäää loadingscreen näkymän
        """
        self.loading_screen.show()

    def show_user_selection_screen(self):
        """
        funktio joka näyttää käyttäjän valinta ja luomis näkymän
        """
        self.loading_screen.hide()
        self.user_selection_screen.show()

    def show_folder_selection_screen(self, user):
        """
        funktio joka näyttää kansion (mindmap) valinta näkymän

        Args:
            user:
                Valitun (tietyn käyttäjän) nimi
        """
        self.user_selection_screen.hide()
        self.folder_selection_screen.show(user)

    def show_mindmap_screen(self):
        """
        funktio joka näyttää mindmap kanvaksen
        """
        self.folder_selection_screen.hide()
        self.mindmap_screen.canvas.pack(fill='both', expand=True)

    def hide_mindmap_screen(self):
        """
        funktio joka piilottaa mindmap kanvaksen
        """
        self.mindmap_screen.canvas.pack_forget()

    def get_user_files_dict(self):
        """
        Tämä metodi hakee ohjelman kansiorakenteesta kansion history sisältämät käyttäjät 
        ja niiden sisältämät tiedostot 
        """
        current_file_path = os.path.abspath(
            inspect.getfile(inspect.currentframe()))
        app_folder_path = os.path.dirname(
            current_file_path)
        tietotila_folder_path = os.path.dirname(
            app_folder_path)
        src_folder_path = os.path.dirname(
            tietotila_folder_path)
        history_path = os.path.join(src_folder_path, "history")
        user_files_dict = {}
        if not os.listdir(history_path):
            return user_files_dict
        for user_folder in os.listdir(history_path):
            user_folder_path = os.path.join(history_path, user_folder)
            if os.path.isdir(user_folder_path):
                pickle_files = []
                for file in os.listdir(user_folder_path):
                    file_path = os.path.join(user_folder_path, file)
                    if os.path.isfile(file_path) and file.endswith('.pickle'):
                        pickle_files.append(file[:-7])
                user_files_dict[user_folder] = pickle_files
        return user_files_dict
