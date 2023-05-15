import sys

from PyQt5.QtWidgets import ( QApplication, )

from app.view.explorer_view import ExplorerWidget
from app.view.main_window import MainWindow


class ExplorerController:
    def __init__(self):
        self.app = QApplication.instance() or QApplication(sys.argv)
        self._main_window = MainWindow()
        self._init_constants()
        self._init_controller()


    def run(self):
        self._main_window.show()
        sys.exit(self.app.exec_())


    def _init_constants(self):
        pass


    def _init_controller(self):
        explorer = ExplorerWidget()
        self._main_window.set_central_widget(explorer)