from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import ( QMainWindow, )


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


    def closeEvent(self, event):
        super().closeEvent(event)


    def resizeEvent(self, event):
        super().resizeEvent(event)


    def changeEvent(self, event):
        super().changeEvent(event)
