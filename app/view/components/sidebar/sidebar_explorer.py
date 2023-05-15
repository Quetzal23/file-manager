from PyQt5.QtWidgets import (
    QWidget,
    QListWidget,
    QVBoxLayout,
)

class SidebarExplorerWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._init_ui()

    def _init_ui(self):
        self.setContentsMargins(0, 0, 0, 0)

        sidebar_list = QListWidget()
        sidebar_list.setContentsMargins(0, 0, 0, 0)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(sidebar_list)
        self.setLayout(layout)