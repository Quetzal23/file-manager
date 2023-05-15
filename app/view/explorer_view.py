from PyQt5.QtWidgets import ( QSplitter, )

from app.view.components.content.file_browser import FileBrowserWidget
from app.view.components.sidebar.sidebar_explorer import SidebarExplorerWidget


class ExplorerWidget(QSplitter):
    def __init__(self):
        super().__init__()
        self._init_ui()


    def _init_ui(self):
        self.setObjectName("")
        self.setContentsMargins(0, 0, 0, 0)

        sidebar = SidebarExplorerWidget()
        browser = FileBrowserWidget()

        self.addWidget(sidebar)
        self.addWidget(browser)

        initial_width = 140
        self.setSizes([initial_width, self.width() - initial_width])