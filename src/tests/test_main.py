from PyQt5.QtWidgets import QApplication
from tietotila.main import main


#testaa ikkunan avautumisen, Otsikon
def test_main(qtbot):
    app = QApplication.instance()
    main_window = main()
    assert main_window.windowTitle() == "Tietotila"
    qtbot.addWidget(main_window)  