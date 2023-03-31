import pytest
import os
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QColor, QPalette
from PyQt5.QtCore import Qt
from tietotila.all_windows import Start  # Update the import path as needed


@pytest.fixture(scope="module")
def app():
    app = QApplication([])
    yield app
    app.quit()


@pytest.fixture
def start_widget(app):
    widget = Start()
    widget.show()
    return widget


def test_init_ui(start_widget):
    assert isinstance(start_widget.layout, QVBoxLayout)
    assert isinstance(start_widget.start_screen, QLabel)


def test_create_window(start_widget):
    label = start_widget.create_window()
    assert isinstance(label, QLabel)
    assert label.autoFillBackground()
    assert label.alignment() == Qt.AlignCenter
    assert label.palette().color(QPalette.Background) == QColor("White")


def test_get_logo(start_widget):
    logo_path = start_widget.get_logo()
    assert os.path.exists(logo_path)
    assert logo_path.endswith("tietotila_startingscreen.jpg")

