import unittest
import tkinter as tk
from unittest.mock import patch
from tietotila.loadingscreen import LoadingScreen


#testloadingscreen.py 
class TestLoadingScreen(unittest.TestCase):
    
    #setup 
    def setUp(self):
        self.window = tk.Tk()
        self.loading_screen = LoadingScreen(self.window)
    
    #näkyykö
    def test_show(self):
        self.loading_screen.show()
        self.assertIn(self.loading_screen.frame, self.window.winfo_children())
    
    #meneekö pois
    def test_hide(self):
        self.loading_screen.show()
        self.loading_screen.hide()
        self.window.after(100, self.check_frame_removed)
    
    #varmistutaan että meni pois
    def check_frame_removed(self):
        self.assertNotIn(self.loading_screen.frame, self.window.winfo_children())
        self.window.quit()
    
    #LoadingScreen-olion on_exit-metodi kutsutaan kun exit-metodia kutsutaan.
    def test_exit_calls_on_exit(self):
        with patch.object(self.loading_screen, 'on_exit') as mock_on_exit:
            self.loading_screen.exit()
            mock_on_exit.assert_called_once()
   
    #olion get_path-metodi palauttaa None-arvon.
    def test_get_path_returns_none(self):
        path = self.loading_screen.get_path()
        self.assertIsNone(path)
    
    #tuhotaan pääikkuna
    def tearDown(self):
        self.window.destroy()


if __name__ == "__main__":
    unittest.main()