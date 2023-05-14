import pytest
from src.tietotila.folders.folder_management import FolderManagement
from tkinter import Tk
from src.tietotila.folders.folder_selection_screen import FolderSelectionScreen  

@pytest.fixture
def setup_folder_selection_screen():
    root = Tk()
    history = {"user1": ["folder1", "folder2"], "user2": ["folder3"]}
    fss = FolderSelectionScreen(root, history)
    return fss

def test_show(setup_folder_selection_screen):
    setup_folder_selection_screen.show("user1")
    assert setup_folder_selection_screen.user == "user1"
    assert len(setup_folder_selection_screen.folders) == 2

def test_update_folder_list(setup_folder_selection_screen):
    setup_folder_selection_screen.show("user1")
    setup_folder_selection_screen.create_folder("new_folder", setup_folder_selection_screen)
    setup_folder_selection_screen.update_folder_list()
    assert "new_folder" in setup_folder_selection_screen.folders

def test_create_folder(setup_folder_selection_screen):
    setup_folder_selection_screen.create_folder("new_folder", setup_folder_selection_screen)
    assert "new_folder" in setup_folder_selection_screen.folders

def test_set_user(setup_folder_selection_screen):
    setup_folder_selection_screen.set_user("user2")
    assert setup_folder_selection_screen.current_user == "user2"

def test_new_folder(setup_folder_selection_screen, monkeypatch):
    monkeypatch.setattr('tkinter.simpledialog.askstring', lambda x, y: "new_folder")
    setup_folder_selection_screen.user = "test_user"  # asettaa käyttäjän
    setup_folder_selection_screen.new_folder()
    assert "new_folder" in setup_folder_selection_screen.folders

