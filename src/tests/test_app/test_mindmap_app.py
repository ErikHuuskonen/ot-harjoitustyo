import tkinter as tk
import pytest
import os
import inspect
from src.tietotila.app.mindmap_app import MindmapApp 


class TestMindmapApp:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.app = MindmapApp()

    def test_init(self):
        assert isinstance(self.app.window, tk.Tk)
        assert isinstance(self.app.history, dict)
    