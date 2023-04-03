import unittest
import tkinter as tk
from tietotila.loadingscreen import LoadingScreen


class TestLoadingScreen(unittest.TestCase):
    def setUp(self):
        self.window = tk.Tk()
        self.loading_screen = LoadingScreen(self.window)

    def test_show(self):
        self.loading_screen.show()
        self.assertTrue(self.loading_screen.frame.winfo_viewable())

    def test_hide(self):
        self.loading_screen.show()
        self.loading_screen.hide()
        self.assertFalse(self.loading_screen.frame.winfo_viewable())

    def tearDown(self):
        self.window.destroy()


if __name__ == "__main__":
    unittest.main()


