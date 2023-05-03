from PyQt5.QtWidgets import (
	QMainWindow,
)


class MainView(QMainWindow):
	def __init__(self, controller):
		QMainWindow.__init__(self)
		self._controller = controller

		self.setContentsMargins(0, 0, 0, 0)
		self.setObjectName("")
