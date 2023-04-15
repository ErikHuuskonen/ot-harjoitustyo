"""
Moduulissa luodaan LoadingScreen-luokka, joka sisältää ikkunan latausnäytölle. 
Luokka alustetaan antamalla sille window-parametrina tkinter-ikkuna, jonka avulla näyttö voidaan näyttää.
"""
import tkinter as tk
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
        image = Image.open("/Users/erikstandard/Desktop/ot-harjoitustyo/resources/tietotila_startingscreen.gif")
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
        
