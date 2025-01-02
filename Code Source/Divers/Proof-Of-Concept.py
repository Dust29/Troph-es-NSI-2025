from PySide6 import QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
from PySide6 import QtCore
from PySide6.QtCore import QTimer
from Comment_ca_marche import *

import sys
from PySide6.QtGui import QPixmap

import keyboard


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Adding Image To Label"
        self.top = 100
        self.left = 500
        self.width = 400
        self.height = 500
        self.InitWindow()

        # Définir un timer pour surveiller les touches
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_key_press)
        self.timer.start(100)  # Vérifier toutes les 100 ms

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setStyleSheet("background-color:#202020")
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.labelImage = QLabel(self)
        pixmap = QPixmap("E:\Vidéo\Ressources\Images\Trucs pour vidéos\Composant\Randy.png")
        pixmap = pixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        self.labelImage.setPixmap(pixmap)
        self.labelImage.move(200, 100)

        self.show()

    def check_key_press(self):
        x = self.labelImage.x()
        y = self.labelImage.y()
        if keyboard.is_pressed("z"):  # Vérifie si "p" est pressé
            print("You pressed z")
            self.labelImage.move(x, y - 30)
            fonction_qui_fait_pas_grand_chose()
        if keyboard.is_pressed("s"):  # Vérifie si "p" est pressé
            print("You pressed s")
            self.labelImage.move(x, y + 30)
        if keyboard.is_pressed("q"):  # Vérifie si "p" est pressé
            print("You pressed q")
            self.labelImage.move(x - 30, y)
        if keyboard.is_pressed("d"):  # Vérifie si "p" est pressé
            print("You pressed d")
            self.labelImage.move(x + 30, y)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

