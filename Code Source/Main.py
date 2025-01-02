from PySide6 import QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
from PySide6 import QtCore
from PySide6.QtCore import QTimer
import keyboard

# Est ce que tout les imports sont utils ?



# Premier ordre du jour : Affichage du "Main Menu" en tile map --> Voir activité pac man


class Fenetre(QDialog):

    #Initisialisation de la fenètre
    def __init__(self) :
        super().__init__()
        self.titre = "Menu Princpical"

        

#bonjour
#au revoir