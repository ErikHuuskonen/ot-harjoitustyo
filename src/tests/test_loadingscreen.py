import unittest
import tkinter as tk
from tietotila.loadingscreen import LoadingScreen
from unittest.mock import MagicMock
from unittest.mock import Mock, patch
from unittest.mock import patch


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

    def test_exit_calls_on_exit(self):
        with patch.object(self.loading_screen, 'on_exit') as mock_on_exit:
            self.loading_screen.exit()
            mock_on_exit.assert_called_once()

    def test_get_path_returns_none(self):
        path = self.loading_screen.get_path()
        self.assertIsNone(path)

    def tearDown(self):
        self.window.destroy()

if __name__ == "__main__":
    unittest.main()




