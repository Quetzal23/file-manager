import sys

from PyQt5.QtWidgets import ( QApplication, )

from app.view.central_widget import CentralWidget
from app.view.main_window import MainWindow


class FileExplorerController:
    def __init__(self):
        self.app = QApplication.instance() or QApplication(sys.argv)
        self.main_window = MainWindow()
        self._init_constants()
        self._init_controller()


    def run(self):
        self.main_window.show()
        sys.exit(self.app.exec_())


    def _init_constants(self):
        pass


    def _init_controller(self):
        central_widget = CentralWidget()
        self.main_window.set_central_widget(central_widget)
