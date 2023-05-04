from PyQt5.QtGui import (
    QIcon,
    QPixmap,
)
from PyQt5.QtCore import ( Qt, )
from PyQt5.QtWidgets import ( QPushButton, )


class RoundButton(QPushButton):
    def __init__(self, size, color='#fff'):
        QPushButton.__init__(self)
        self.setFixedSize(size, size)
        # self.setIcon(QIcon(icon_path))
        self.setIconSize(self.size())
        self.setStyleSheet(f"background-color: {color}; border-radius: {size//2}px; border: none;")


    def set_icon(self, icon):
        width = int(self.width() - 6)
        height = int(self.height() - 6)

        pixmap = QPixmap(icon)
        pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setIcon(QIcon(pixmap))