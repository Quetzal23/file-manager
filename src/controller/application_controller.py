import sys

from PyQt5.QtCore import ( Qt, )
from PyQt5.QtWidgets import ( QApplication, )

from src.controller.app_controller import AppController
from src.controller.main_controller import MainController
from src.view.main_window import MainWindow


class AplicationController:
    # Controlador que se encarga de iniciar la aplicacion
    def __init__(self):
        super().__init__()
        # Habilita el escalado automatico en funcion de la densidad de pixeles del monitor
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

        # Instancia de la clase QAplication que utiliza argumentos de linea de comandos
        # para iniciar la aplicacion
        self.app = QApplication(sys.argv)
        self.main_window = MainWindow()    # Intancia de la ventana principal
        self.init_controller()  # Instancias de los controladores

        # LLamando el evento de cierre de ventana de la aplicacion
        self.main_window.closeEvent = self.close


    def close(self, event):
        # Cierre de los controladores antes de cerrar la aplicacion
        self.app_controller.close() # Cierre de los mvc
        self.main_controller.close()    # Cierre de las conexiones
        event.accept()  # Acepta el evento de cierre


    def run(self):
        # Iniciando los controladores
        self.app_controller.run()
        self.main_controller.run()

        # Iniciando la ventana principal
        self.main_window.show() # Mostrando la ventana principal
        sys.exit(self.app.exec_())  # Ejecución de la aplicación


    def init_controller(self):
        # Instancia de los controladores
        self.app_controller = AppController()   # Instacia del controlador que se encarga de las conexiones
        self.main_controller = MainController(self.main_window, self.app_controller) # Instacia del controlador que se encarga de cargar los mvc
