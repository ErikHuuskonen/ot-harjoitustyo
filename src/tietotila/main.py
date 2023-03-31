from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer 
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

import sys
from all_windows import Start, Users, Mindmap

def main():
    #aloitus screen
    app = QApplication(sys.argv)

    # Create main window and widgets
    main_window = QMainWindow()
    start = Start()
    users = Users()
    mindmap = Mindmap()

    #näytä aloitus näyttö Start
    main_window.setCentralWidget(start)
    main_window.showFullScreen()

    #viiden sekunnin jälkeen näytetään Users
    QTimer.singleShot(5000, lambda: main_window.setCentralWidget(users))
    
    #users näyttää keskellä näyttöä neliskulmaisen harmaan napin jota painamalla voimme kirjoittaa uuden käyttäjän nimen ja tämä asetus astuu voimaan.
    
    #nyt voimme valita käyttäjän ja sen sisälle avautuu valikko jonka sisällä on neljä vaihtoehtoista tiedon arkistoa.

    #astumme tiedon arkistoon ja siellä näemme avautuneen mind mapin jonka sisällä voimme astua taas uuteen mindmappiin jonka masted node on se otsikko jota klikkasimme.

    sys.exit(app.exec_())

if __name__=="__main__":
    main()