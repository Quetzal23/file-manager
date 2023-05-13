import sys

from PyQt5.QtWidgets import ( QApplication, )

from app.view.main_window import MainWindow


class FileExplorerController:
    def __init__(self):
        self.app = QApplication.instance() or QApplication(sys.argv)
        self.main_window = MainWindow()


    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec_())
