import unittest
from tkinter import Tk
from tietotila.users.user_selection_screen import UserSelectionScreen
from tietotila.folders.folder_selection_screen import FolderSelectionScreen
from tietotila.users.user_management import UserManagement
from unittest.mock import Mock
from unittest.mock import patch

# test UserSelectionScreen


class TestUserSelectionScreen(unittest.TestCase):

    # pystytetään
    @classmethod
    def setUpClass(cls):
        cls.window = Tk()
    # tuhotaan

    @classmethod
    def tearDownClass(cls):
        cls.window.destroy()

    # setup
    def setUp(self):
        self.window = Tk()
        self.history = {}
        self.folder_selection_screen = FolderSelectionScreen(self.window, self.history)
        self.user_selected_callback = Mock()
        self.user_management = UserManagement(
            self.window, self.folder_selection_screen, self.user_selected_callback)
        self.user_selection_screen = UserSelectionScreen(
            self.window, self.user_management, self.history)

    # testaa käyttöliittymän otsikko- ja nappitekstien oikeellisuutta
    def test_init(self):
        self.assertEqual(
            self.user_selection_screen.title_label["text"], "Valitse käyttäjä")
        self.assertEqual(
            self.user_selection_screen.new_user_button["text"], "New User")

    # testaa, että käyttöliittymän piilottaminen toimii oikein.
    def test_hide(self):
        self.user_selection_screen.show()
        self.user_selection_screen.hide()
        self.assertFalse(self.user_selection_screen.frame.winfo_ismapped())

    # testaa uuden käyttäjän luomistoiminnallisuuden oikeellisuutta, kun käyttäjänimi annetaan syötteenä.
    def test_create_new_user(self):
        with patch("tkinter.simpledialog.askstring", return_value="New User"), \
                patch.object(self.user_management, "create_user") as mocked_create_user:
            self.user_selection_screen.create_new_user()
        mocked_create_user.assert_called_once_with(
            "New User", self.user_selection_screen.frame)

    # testaa käyttäjän valinnan oikeellisuutta
    def test_select_user(self):
        self.user_selection_screen.on_user_selected = Mock()
        self.user_selection_screen.select_user("test_user")
        self.user_selection_screen.on_user_selected.assert_called_once_with(
            "test_user")

    


if __name__ == "__main__":
    unittest.main()
