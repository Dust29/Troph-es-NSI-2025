import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QImage
from PyQt5.QtCore import QTimer, QElapsedTimer, QPoint

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5")
        self.resize(512, 256)
        # Download a sprite sheet here:
        # https://plnkr.co/edit/zjYT0KTfj50MejT9?preview
        self.sprite_sheet = QImage("P:\\Documents\\NSI\\Trophées\\Ressources\\sprites-cat-running.png") #Changer ca en fonction de la machine
        self.sw = 512
        self.sh = 256
        self.frame_index = 0
        self.x = 0
        self.y = 0
        self.frames = []
        for i in range(2):
            for j in range(4):
                self.frames.append(QPoint(j * self.sw, i * self.sh))
        self.delta_time = 0
        self.animation_time = 0
        self.animation_speed = 100
        self.timer = QTimer()
        self.timer.timeout.connect(self.animationLoop)
        self.elapsedTimer = QElapsedTimer()
        self.timer.start(int(1000/60))
        
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
        self.update()

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.drawImage(0, 0, self.sprite_sheet, self.x, self.y, self.sw, self.sh)

def main():
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

