from PyQt5.QtWidgets import (
    QTabBar,
    QPushButton,
)


class ClosableTabWidget(QTabBar):
    def __init__(self, parent=None):
        super().__init__(parent)


    def _init_ui(self):
        self.tabCloseRequested.connect(self._close_tab)


    def _close_tab(self, index):
        self.parent().removeTab(index)


    def addClosableTab(self, widget, title):
        self.parent().addTab(widget, title)
        close_button = QPushButton(self)
        close_button.clicked.connect(lambda: self._close_tab(self.parent().indexOf(widget)))
        self.setTabButton(self.parent().indexOf(widget), QTabBar.RightSide, close_button)
