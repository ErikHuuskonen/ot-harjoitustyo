"""
Tämä muduuli luo käyttöliittymän mindmap-sovellukselle. 
Sovelluksessa käyttäjä voi luoda mindmap-näkymän, lisätä solmuja ja 
navigoida mindmapin eri osien välillä. 
Moduulissa käytetään tkinter-kirjastoa käyttöliittymän rakentamiseen, 
ja siinä on luokkia, jotka vastaavat eri näkymistä ja käyttöliittymän toiminnallisuuksista.
"""
import tkinter as tk
from usermanagement import UserManagement
from loadingscreen import LoadingScreen
from userselectionscreen import UserSelectionScreen
from folderselectionscreen import FolderSelectionScreen
from mindmapscreen import MindMap
class MindmapApp:
    """
    Tämä luokka muodostaa mindmap sovelluksen käyttämiseen tarvittavat moduulit ja luokat. 
    Se sisältää funktiot eri näkyminen välillä siirtymiseen sekä kutsuu kunkin moduulin luokan konstruktoria.
    """
    def __init__(self):
        """
        Luokan rakentaja, joka luo Mindmapapp-objektin.
        """
        self.window = tk.Tk()
        self.window.geometry('1000x1200')
        self.window.title("Tietotila")
        self.loading_screen = LoadingScreen(self.window)
        self.user_management = UserManagement(self.window, self.show_folder_selection_screen, self.show_folder_selection_screen)
        self.user_selection_screen = UserSelectionScreen(self.window, self.user_management)
        self.folder_selection_screen = FolderSelectionScreen(self.window, self.show_mindmap_screen)
        self.user_management = UserManagement(self.window, self.folder_selection_screen, self.show_folder_selection_screen)
        self.mindmap_screen = MindMap(self.window)#self.mindmap_management)
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