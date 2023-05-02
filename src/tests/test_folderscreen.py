import unittest
from unittest.mock import patch, Mock
from tkinter import Tk, Button
from tkinter.simpledialog import SimpleDialog
from tkinter.simpledialog import askstring

from tietotila.folderselectionscreen import FolderSelectionScreen
# from tietotila.mindmapapp import MindmapApp
# from tietotila.mindmapscreen import MindMap
# from tietotila.usermanagement import UserManagement


class TestFolderSelectionScreen(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.window = Tk()

    @classmethod
    def tearDownClass(cls):
        cls.window.destroy()

    def setUp(self):
        self.screen = FolderSelectionScreen(self.window)

    def test_init(self):
        self.assertIsInstance(self.screen.new_folder_button, Button)
        self.assertEqual(self.screen.new_folder_button["text"], "New Folder")

    def test_show(self):
        self.screen.update_folder_list = Mock()
        self.screen.show("test_user")
        self.assertEqual(self.screen.user, "test_user")
        self.screen.update()
        self.assertTrue(self.screen.winfo_ismapped())
        self.screen.update_folder_list.assert_called_once()

    def test_hide(self):
        self.screen.hide()
        self.assertFalse(self.screen.winfo_ismapped())

    # @patch.object(SimpleDialog, "askstring", return_value="test_folder")
    # @patch.object(FolderSelectionScreen, "create_folder")
    # def test_create_new_folder(self, mocked_create_folder, mocked_askstring):
        # self.screen.create_new_folder()
       # mocked_askstring.assert_called_once_with("Uusi tila", "Syötä tilan nimi:")
        # mocked_create_folder.assert_called_once_with("test_folder", self.screen)

    def test_update_folder_list(self):
        self.screen.folders = ["folder1", "folder2"]
        self.screen.update_folder_list()
        # New folder button + 2 folder buttons
        self.assertEqual(len(self.screen.winfo_children()), 3)
        folder1_button, folder2_button = self.screen.winfo_children()[1:]
        self.assertEqual(folder1_button["text"], "folder1")
        self.assertEqual(folder2_button["text"], "folder2")

    def test_create_folder(self):
        self.screen.create_folder("test_folder", self.screen)
        self.assertEqual(len(self.screen.folders), 1)
        self.assertEqual(self.screen.folders[0], "test_folder")
        # New folder button + 1 folder button
        self.assertEqual(len(self.screen.winfo_children()), 2)
        folder_button = self.screen.winfo_children()[1]
        self.assertEqual(folder_button["text"], "test_folder")

    def test_folder_button_pressed(self):
        self.screen.on_mindmap_selected = Mock()
        self.screen.folder_button_pressed("test_folder")
        self.screen.on_mindmap_selected.assert_called_once()

    # @patch.object(SimpleDialog, "askstring", return_value="test_folder")
    # def test_new_folder(self, mocked_askstring):
        # self.screen.folders = []
        # self.screen.update_folder_list = Mock()
        # self.screen.new_folder()
       # mocked_askstring.assert_called_once_with("New Folder", "Enter folder name:")
       # self.assertEqual(len(self.screen.folders), 1)
       # self.assertEqual(self.screen.folders[0], "test_folder")
       # self.screen.update_folder_list.assert_called_once()


if __name__ == "__main__":
    unittest.main()
