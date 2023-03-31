from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer 
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

import sys
from all_windows import Start, Users, Documents, Mindmap

def main():
    app = QApplication(sys.argv)
    # Create main window and widgets
    main_window = QMainWindow()
    mindmap = Mindmap()
    main_window.setCentralWidget(mindmap)
    main_window.showFullScreen()
    sys.exit(app.exec_())

def main_1():
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    users = Users()
    main_window.setCentralWidget(users)
    main_window.showFullScreen()
    sys.exit(app.exec_())

def main_2():
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    main = Documents()
    main_window.setCentralWidget(main)
    main_window.showFullScreen()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()


