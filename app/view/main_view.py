import sys
from PyQt5.QtCore import ( Qt, )
from PyQt5.QtWidgets import (
	QWidget,
	QTabWidget,
	QMainWindow,
	QApplication,
	QDesktopWidget,
)

from app.classes.stylessheet import StylesSheet
from app.view.components.widgets.custom_corner_tabwidget import CustomCornerTabWidget
from app.view.components.widgets.custom_tabar import CustomTabBar
from constants import CSS_DIR


class MainView(QMainWindow):
	isMaximized = True

	def __init__(self, controller):
		QMainWindow.__init__(self)
		self._controller = controller

		self._app = QApplication.instance()

		self.add_style()

		self.setObjectName("")
		self.setContentsMargins(0, 0, 0, 0)
		self.setWindowFlag(Qt.FramelessWindowHint)

		self._set_geometry()
		self.showMaximized()

		try:
			self._main_container()
		except Exception as e:
			print(f"Exception in main_view.MainView: {e}")


	def _set_geometry(self):
		scr = self._app.desktop().screenGeometry()
		width = int(scr.width() - 340)
		height = int(scr.height() - 100)
		return self.setGeometry(0, 0, width, height)


	def add_style(self):
		style = StylesSheet(CSS_DIR + 'styles.qss')
		self._app.setStyleSheet(style.stylesheet())


	def _main_container(self):
		self.main_tab = QTabWidget()
		self.main_tab.setContentsMargins(0, 0, 0, 0)
		self.setCentralWidget(self.main_tab)

		self._corner_widget = CustomCornerTabWidget()
		_minimize_button = self._corner_widget.minimize_button
		_maximize_button = self._corner_widget.maximize_button
		_close_button = self._corner_widget.close_button

		_minimize_button.clicked.connect(self.showMinimized)
		_maximize_button.clicked.connect(self.show_maximized)
		_close_button.clicked.connect(self.closeEvent)

		self.main_tab.setTabBar(CustomTabBar())
		self.main_tab.setCornerWidget(self._corner_widget)

		self.tab1 = QWidget()
		self.main_tab.addTab(self.tab1, "Pestaña 1")


	def resizeEvent(self, event):
		if not self.isMaximized:
			center = QDesktopWidget().availableGeometry().center()
			frame_geometry = self.frameGeometry()
			frame_geometry.moveCenter(center)
			self.move(frame_geometry.topLeft())


	def show_maximized(self):
		print(self.isMaximized)
		if not self.isMaximized:
			self._corner_widget.show_maximize()
			self.showMaximized()
			self.isMaximized = True
		else:
			self._corner_widget.show_normal()
			self.showNormal()
			self.isMaximized = False


	def closeEvent(self, event):
		sys.exit()