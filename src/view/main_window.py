from PyQt5.QtCore import ( QEvent, )
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QDesktopWidget,
)


class MainWindow(QMainWindow):
    _is_maximized = False   # Detecta el estado de la ventana

    def __init__(self):
        super().__init__()
        self.init_constants()
        self.init_ui()


    def closeEvent(self, event):
        # Maneja el evento de cambio de estado de la ventana
        if event.type() == QEvent.WindowStateChange:
            if self.isMaximized():
                self._is_maximized = True
            elif self._is_maximized:
                self._is_maximized = False
                self.center_window()
        super().closeEvent(event)


    def resizeEvent(self, event):
        # Maneja el evento de cambio de tamaño de la ventana
        if self.isMaximized() or self.isFullScreen():
            self._is_maximized = True
        else:
            self.center_window()
        super().resizeEvent(event)


    def changeEvent(self, event):
        # Maneja el evento de cambio de estado de la ventana
        if event.type() == QEvent.WindowStateChange:
            if self.isMaximized():
                self._is_maximized = True
            elif self._is_maximized:
                self._is_maximized = False
                self.center_window()
        super().changeEvent(event)


    def init_constants(self):
        self.app = QApplication.instance()  # Instancia de la aplicación


    def init_ui(self):
        # Configuración de la ventana principal
        self.setContentsMargins(0, 0, 0, 0) # Margenes de la vista
        self.setProperty("class", "")   # Nombre de clase
        self.set_window_geometry()  # Geometria de la ventana
        self.showMaximized()    # Maximar la ventana


    def set_window_geometry(self):
        # Configurar la geometria de la ventana
        screen = QDesktopWidget().availableGeometry()
        width = int(screen.width() * 0.8)    # 80% del ancho de la pantalla
        height = int(screen.height() * 0.8)  # 80% de la altura de la pantalla
        x = (screen.width() - width) // 2    # Centrar horizontalmente
        y = (screen.height() - height) // 2  # Centrar verticalmente
        self.setGeometry(x, y, width, height)   # Establece la geometria


    def center_window(self):
        # Centra la ventana en la pantalla
        screen_geometry = QDesktopWidget().screenGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.setGeometry(x, y, self.width(), self.height())
