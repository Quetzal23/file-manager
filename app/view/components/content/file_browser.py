from PyQt5.QtWidgets import (
    QWidget,
)


class FileBrowserWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setContentsMargins(0, 0, 0, 0)