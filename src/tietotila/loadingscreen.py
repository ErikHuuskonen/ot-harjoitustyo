"""
Moduulissa luodaan LoadingScreen-luokka, joka sisältää ikkunan latausnäytölle. 
Luokka alustetaan antamalla sille window-parametrina tkinter-ikkuna, jonka avulla näyttö voidaan näyttää.
"""
import tkinter as tk
import os
import sys
from PIL import Image, ImageTk
class LoadingScreen:
    """
    LoadingScreen-luokka, joka sisältää ikkunan latausnäytölle. 
    Luokka alustetaan antamalla sille window-parametrina tkinter-ikkuna, jonka avulla näyttö voidaan näyttää.
    """
    def __init__(self, window):
        """
        Luokan rakentaja, joka luo uuden LoadingScreen-objektin.
        Args:
        window (tk.Tk): juuri-ikkuna, johon latausnäyttö tulee.
        """
        self.window = window
        self.frame = tk.Frame(self.window)
        self.image_name = "tietotila_startingscreen.gif"
        self.image_path = self.get_path()
        image = Image.open(self.image_path)
        photo = ImageTk.PhotoImage(image)
        self.image_label = tk.Label(self.frame, image=photo)
        self.image_label.image = photo
        self.image_label.pack(pady=10)
        self.loading_label = tk.Label(self.frame, text="Loading Screen")
        self.loading_label.pack(pady=10)
        self.on_exit = None
        self.exit_button = tk.Button(self.frame, text="Continue", command= self.exit, fg="black")
        self.exit_button.place(x=100, y=100)
        self.exit_button.pack(pady=10)
        self.window.after(5000, self.exit)
    def show(self):
        """
        Metodi, joka näyttää latausnäytön.
        """
        self.frame.pack(fill=tk.BOTH, expand=True)
    def hide(self):
        """
        Metodi, joka piilottaa latausnäytön.
        """
        self.frame.pack_forget()
    def exit(self):
        """
        Metodi, joka sulkee latausnäytön.
        """
        if self.on_exit:
            self.on_exit()
    def get_path(self):
        """
        Metodi, joka hakee aloitusnäytön kuvan.
        """
        def get_project_root():
            current_file_path = os.path.abspath(__file__)
            while not os.path.basename(current_file_path) == "ot-harjoitustyo":
                current_file_path = os.path.dirname(current_file_path)
            return current_file_path
            # Tarkista käyttöjärjestelmä
        platform = sys.platform
        project_directory = get_project_root()
        image_directory_name = "resources"
        if platform == "win32":
            image_directory_path = os.path.join(project_directory, image_directory_name)
        elif platform == "darwin":
            image_directory_path = os.path.join(project_directory, image_directory_name)
        elif platform.startswith("linux"):
            image_directory_path = os.path.join(project_directory, image_directory_name)
        else:
            raise ValueError("Tuntematon käyttöjärjestelmä: " + platform)
        image_path = os.path.join(image_directory_path, self.image_name)
        return image_path  