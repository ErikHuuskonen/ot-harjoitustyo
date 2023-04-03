import unittest
import tkinter as tk
from tietotila.loadingscreen import LoadingScreen

class TestLoadingScreen(unittest.TestCase):
    def setUp(self):
        self.window = tk.Tk()
        self.loading_screen = LoadingScreen(self.window)

    def test_show(self):
        self.loading_screen.show()
        self.assertIn(self.loading_screen.frame, self.window.winfo_children())

    def test_hide(self):
        self.loading_screen.show()
        self.loading_screen.hide()
        self.window.after(100, self.check_frame_removed)

    def check_frame_removed(self):
        self.assertNotIn(self.loading_screen.frame, self.window.winfo_children())
        self.window.quit()

    def tearDown(self):
        self.window.destroy()

if __name__ == "__main__":
    unittest.main()




