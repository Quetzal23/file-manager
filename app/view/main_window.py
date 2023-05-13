from PyQt5.QtGui import (
    QFont,
    QResizeEvent,
)
from PyQt5.QtCore import ( QTranslator, )
from PyQt5.QtWidgets import (
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QApplication,
    QDesktopWidget,
)

from app.classes.established_font import EstablishedFont
from app.classes.established_stylesheet import EstablishedStylesheet
from app.classes.established_text import EstablishedText
from app.classes.established_translation import EstablishedTranslation
from constants import CSS_DIR, FONT_DIR, LANG_DIR


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._init_constants()
        self._init_ui()


    def _init_constants(self):
        self._app = QApplication.instance()

        window_lang = LANG_DIR
        window_text = LANG_DIR + 'default.txt'
        window_css = CSS_DIR + 'styles.qss'
        window_font = FONT_DIR

        self._setup_translation(window_lang)
        self._setup_text_widgets(window_text)
        self._setup_styles(window_css, window_font)


    def _setup_translation(self, window_lang):
        translation = EstablishedTranslation('file-manager', window_lang, 'default')
        translator = QTranslator()
        translator.load(translation.gettext())
        self._app.installTranslator(translator)


    def _setup_text_widgets(self, window_text):
        text_widgets = EstablishedText()
        text_widgets.load_file_text(window_text)


    def _setup_styles(self, window_css, window_font):
        stylesheet = EstablishedStylesheet(window_css)
        font_family = EstablishedFont(window_font)

        self._app.setStyleSheet(stylesheet.stylesheet())
        for f in font_family.get_font_families():
            font = QFont(f)
            self._app.setFont(font)


    def _init_ui(self):
        self.setContentsMargins(0, 0, 0, 0)
        self.setObjectName("")

        self.setup_ui()
        self.update_screen_size()
        self.showMaximized()


    def setup_ui(self):
        self.central_layout = QVBoxLayout()
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        central_widget = QWidget()
        central_widget.setContentsMargins(0, 0, 0, 0)
        central_widget.setObjectName("")
        central_widget.setLayout(self.central_layout)
        self.setCentralWidget(central_widget)


    def update_screen_size(self):
        screen_size = QDesktopWidget().screenGeometry()
        width = screen_size.width() - 340
        height = screen_size.height() - 100
        self.setGeometry(0, 0, width, height)


    def screen_geometry(self):
        screen_geometry = QDesktopWidget().availableGeometry().center()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry)
        self.move(window_geometry.topLeft())


    def resizeEvent(self, event: QResizeEvent):
        if self.isMaximized:
            self.screen_geometry()
        super().resizeEvent(event)
