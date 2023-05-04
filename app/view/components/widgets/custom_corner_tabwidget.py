from PyQt5.QtCore import ( Qt, )
from PyQt5.QtWidgets import (
    QLabel,
    QWidget,
    QHBoxLayout,
)

from app.view.components.buttons.round_button import RoundButton
from constants import SVG_DIR


class CustomCornerTabWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setContentsMargins(0, 0, 0, 0)

        self._flags_icon = (
            SVG_DIR + 'math-minus-svgrepo-com.svg',
            SVG_DIR + 'minimize-svgrepo-com.svg',
            SVG_DIR + 'maximize-svgrepo-com.svg',
            SVG_DIR + 'close-svgrepo-com.svg'
        )

        self.minimize_button = RoundButton(20, 'white')
        self.maximize_button = RoundButton(20, 'white')
        self.close_button = RoundButton(20, 'red')

        self.minimize_button.set_icon(self._flags_icon[0])
        self.maximize_button.set_icon(self._flags_icon[1])
        self.close_button.set_icon(self._flags_icon[3])

        main_layout = QHBoxLayout()
        main_layout.setSpacing(8)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        main_layout.addWidget(self.minimize_button)
        main_layout.addWidget(self.maximize_button)
        main_layout.addWidget(self.close_button)

        label = QLabel()
        label.setFixedHeight(25)
        label.setFixedWidth(100)
        label.setContentsMargins(0, 0, 0, 0)
        # label.setStyleSheet("background: red;")
        label.setLayout(main_layout)

        layout = QHBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)


    def show_maximize(self):
        self.maximize_button.set_icon(self._flags_icon[1])


    def show_normal(self):
        self.maximize_button.set_icon(self._flags_icon[2])