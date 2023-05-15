from PyQt5.QtWidgets import (
    QTabWidget,
    QVBoxLayout,
)

from app.view.components.tab.close_tab import ClosableTabWidget


class CentralWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("")
        self.setContentsMargins(0, 0, 0, 0)
        self._init_constants()
        self._init_ui()


    def _init_constants(self):
        pass


    def _init_ui(self):
        close_tab = ClosableTabWidget(self)
        self.setTabBar(close_tab)

        self._central_layout = QVBoxLayout()
        self._central_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self._central_layout)
