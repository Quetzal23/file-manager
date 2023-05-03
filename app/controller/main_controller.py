import sys
from PyQt5.QtWidgets import ( QApplication, )

from app.view.main_view import MainView


class MainController:
	def __init__(self):
		self._app = QApplication(sys.argv)
		self._view = MainView(self)


	def run(self):
		try:
			self._view.show()
			sys.exit(self._app.exec_())
		except Exception as e:
			print(f"Exception in controller.MainController: {e}")
