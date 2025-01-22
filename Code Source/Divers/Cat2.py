import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QImage
from PySide6.QtCore import QTimer, QElapsedTimer, QPoint
from PySide6 import QtGui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel
from PySide6 import QtCore
from PySide6.QtCore import QTimer

#TODO Mettre l'elf au dessus du background

#Marche en PySide6

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5")
        self.resize(1920, 1080)
        
        # Download a sprite sheet here:
        # https://plnkr.co/edit/zjYT0KTfj50MejT9?preview
        self.sprite_sheet = QImage(".\\ELF_RUN1_corrigé.gif")
        self.sw = 64+16 #Original + buffer
        self.sh = 84
        self.frame_index = 0
        self.x = 0
        self.y = 0
        self.frames = []
        self.dec=256
        flag = True
        for i in range(2):
            for j in range(4):
                self.frames.append(QPoint(j * self.sw, i * self.sh))
                
        self.delta_time = 0
        self.animation_time = 0
        self.animation_speed = 100
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animationLoop)
        
        self.elapsedTimer = QElapsedTimer()
        self.elapsedTimer.start()
        self.timer.start(int(100/60))   #Boucle pour l'animation
        self.a=True
        self.LabelList = [[0] * 32 for i in range(32)] #Changer les dimensions si besoin
        self.tileMap = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],                   
                   [0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
            
        self.background()
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.animationLoop)
#         self.elapsedTimer = QElapsedTimer()
#         self.timer.start(int(1000/60))
         
    def animationLoop(self):
        self.delta_time = self.elapsedTimer.elapsed()
        self.elapsedTimer.restart()
        self.animation_time += self.delta_time
        if self.animation_time >= self.animation_speed:
            self.animation_time = 0
            self.x = self.frames[self.frame_index].x()
            self.y = self.frames[self.frame_index].y()
            self.frame_index += 1
            if self.frame_index >= len(self.frames):
                self.frame_index = 0
            self.dec+=20
        self.update()

    def paintEvent(self, event):
        print(event)
        qp = QPainter(self)
        qp.drawImage(0+self.dec, 0, self.sprite_sheet, self.x, self.y, self.sw, self.sh)
        if self.a:self.tileMap[0][0]=1
        else:self.tileMap[0][0]=0
        self.a=not self.a
        
        
    def background(self):
        ListOfPath = [".\\tiles\\regularTile.png",".\\tiles\\bricksTile.png",]
        
        
        #La carte est dans le mauvais sens (90° sur la gauche)
        
        
        
        
        #TODO Ajouter dictionnaire + gestion par tilemap
        
        for i in range(int(512/16)): # Colonne 
            for j in range(int(512/16)): #Ligne
            
                self.labelImage = QLabel(self)
                self.LabelList[j][i] = self.labelImage
                pixmap2 = QPixmap(ListOfPath[self.tileMap[j][i]])
                pixmap2.depth = 64
                print(pixmap2)
                #pixmap2 = pixmap2.scaled(16, 16, QtCore.Qt.KeepAspectRatio)
                self.LabelList[j][i].setPixmap(pixmap2)
                self.LabelList[j][i].move(16*i, 16*j)
                #print(f"Moved {i} {j} to {16*i} {16*j}")
        
       

#         self.labelImage = QLabel(self)
#         LabelList.append(self.labelImage)
#         pixmap = QPixmap("F:\\DEV\\Trophèes '25\\Repo Github\\Code Source\\Divers\\MAXI_BL2.GIF")
#         pixmap = pixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
#         LabelList[1].setPixmap(pixmap)
#         LabelList[1].move(200, 100)

def main():
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



