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

        # La taille est défini d'une facon un peu bizarre :
        # left et top sont les cos de "départs" (L'origine de la fenètre)
        # Largeur et Hauteur sont les dimensions.
        # Assumons que l'écran est en 1920*1080

        # Les "marges" sur le coté sont les suivantes :
        # 1/3 de 1920 de chaque coté. (si largeur = 768)

        self.left = 576
        self.top = 200  # Valeur aléatoire

        # Vrai "taille" de la fenètre
        self.largeur = 768
        self.hauteur = 300 # Valeur aléatoire

        self.InitWindow()

        # Définir un timer pour surveiller les touches
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_key_press)
        self.timer.start(100)  # Vérifier toutes les 100 ms
#ewenn