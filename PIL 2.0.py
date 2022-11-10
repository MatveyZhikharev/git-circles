import sys

from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap, QBitmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class MyPillow(QMainWindow):
    def __init__(self):
        super(MyPillow, self).__init__()
        uic.loadUi("cat.ui", self)
        self.app = app

        self.filename = QFileDialog.getOpenFileName(self, "Выберете картинку", "", "Картинки (*.jpg)")[0]

        self.orig_photo = Image.open(self.filename)
        self.cor_photo = Image.open(self.filename)
        self.degree = 0

        self.a = ImageQt(self.cor_photo)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)
        for button in self.chanel_buttons.buttons():
            button.clicked.connect(self.set_chanel)
        for button in self.rotate_buttons.buttons():
            button.clicked.connect(self.rotate)

    def set_chanel(self):
        self.cor_photo = self. orig_photo.copy()
        pixels = self.cor_photo.load()
        x, y = self.cor_photo.size
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                if self.sender().text() == "R":
                    pixels[i, j] = (r, 0, 0)
                elif self.sender().text() == "G":
                    pixels[i, j] = (0, g, 0)
                elif self.sender().text() == "B":
                    pixels[i, j] = (0, b, 0)
        self.cor_photo = self.cor_photo.rotate(self.degree, expand=True)
        self.a = ImageQt(self.cor_photo)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)

    def rotate(self):
        if self.sender() is self.pushButton_3:
            self.degree -= 90
            degree = -90
        else:
            self.degree += 90
            degree = 90
        self.degree %= 360
        self.cor_photo = self.cor_photo.rotate(degree, expand=True)
        self.a = ImageQt(self.cor_photo)
        self.pixmap = QPixmap.fromImage(self.a)
        self.image.setPixmap(self.pixmap)


def excepthook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())
