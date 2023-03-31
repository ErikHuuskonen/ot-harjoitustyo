
from PyQt5.QtWidgets import QPushButton
from tietotila.all_windows import Users  


def test_users_initial_state(qtbot):
    users = Users()
    qtbot.addWidget(users)
    assert len(users.users_list) == 0
    assert users.layout is not None
    assert users.hbox_layout is not None

def test_users_empty_button(qtbot):
    users = Users()
    qtbot.addWidget(users)
    empty_button = users.findChild(QPushButton, "Uusi käyttäjä")
    assert empty_button is not None


