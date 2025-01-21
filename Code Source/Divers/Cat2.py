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
#TODO le background avec un dictionnaire

#Marche en PySide6

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5")
        self.resize(1920, 1080)
        # Download a sprite sheet here:
        # https://plnkr.co/edit/zjYT0KTfj50MejT9?preview
        self.sprite_sheet = QImage("F:\\DEV\\Trophèes '25\\Repo Github\\Code Source\\Divers\\ELF_RUN1_corrigé.gif")
        self.sw = 64+16 #Original + buffer
        self.sh = 84
        self.frame_index = 0
        self.x = 0
        self.y = 0
        self.frames = []
        self.dec=0
        flag = True
        for i in range(2):
            for j in range(4):
                self.frames.append(QPoint(j * self.sw, i * self.sh))
                
        
        self.background()
        
        self.delta_time = 0
        self.animation_time = 0
        self.animation_speed = 100
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animationLoop)
        
        self.elapsedTimer = QElapsedTimer()
        self.elapsedTimer.start()
        self.timer.start(int(1000/60))   #Boucle pour l'animation
        
        
        
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
        qp = QPainter(self)
        qp.drawImage(0+self.dec, 0, self.sprite_sheet, self.x, self.y, self.sw, self.sh)
        
    def background(self):
        ListOfPath = [".\\tiles\\regularTile.png",".\\tiles\\bricksTile.png",]
        LabelList = [[0] * 16 for i in range(32)] #Changer les dimensions si besoin
        
        for i in range(int(512/16)):
            for j in range(int(256/16)):
            
                self.labelImage = QLabel(self)
                LabelList[i][j] = self.labelImage
                pixmap2 = QPixmap(ListOfPath[i%2])
                pixmap2 = pixmap2.scaled(16, 16, QtCore.Qt.KeepAspectRatio)
                LabelList[i][j].setPixmap(pixmap2)
                LabelList[i][j].move(16*i, 16*j)
                print(f"Moved {i} to {16*i} {16*j}")
        
        
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


