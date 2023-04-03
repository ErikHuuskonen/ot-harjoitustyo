#ohjelman arkkitehtuurissa on käytetty Chat-GTP 4:sta
import tkinter as tk
from usermanagement import UserManagement
#from mindmapmanagement import MindmapManagement
from loadingscreen import LoadingScreen
from userselectionscreen import UserSelectionScreen
#from folderselectionscreen import FolderSelectionScreen
#from mindmapscreen import MindmapScreen

class MindmapApp:
    def __init__(self):
        self.user_management = UserManagement()
        #self.mindmap_management = MindmapManagement()
        
        self.window = tk.Tk()
        self.window.title("Tietotila")
        self.window.geometry('500x500')
        
        # Initialize the app components
        self.loading_screen = LoadingScreen(self.window)
        self.user_selection_screen = UserSelectionScreen(self.window, self.user_management)
        #self.folder_selection_screen = FolderSelectionScreen(self.window, self.user_management, self.mindmap_management)
        #self.mindmap_screen = MindmapScreen(self.window, self.mindmap_management)
        
        # Configure the app flow
        self.loading_screen.on_exit = self.show_user_selection_screen
        #self.user_selection_screen.on_user_selected = self.show_folder_selection_screen
        #self.folder_selection_screen.on_mindmap_selected = self.show_mindmap_screen
        #self.mindmap_screen.on_exit = self.show_folder_selection_screen

    def run(self):
        self.show_loading_screen()
        self.window.mainloop()

    def show_loading_screen(self):
        self.loading_screen.show()

    def show_user_selection_screen(self):
        self.loading_screen.hide()
        self.user_selection_screen.show()

    #def show_folder_selection_screen(self, user):
        #self.user_selection_screen.hide()
        #self.folder_selection_screen.show(user)

    #def show_mindmap_screen(self, mindmap):
        #self.folder_selection_screen.hide()
        #self.mindmap_screen.show(mindmap)

    def user_selected(self, user):
        print(f"User selected: {user}")


