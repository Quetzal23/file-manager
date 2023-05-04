from PyQt5.QtGui import (
    QColor,
    QPainter,
)
from PyQt5.QtCore import (
    Qt,
    QSize,
)
from PyQt5.QtWidgets import (
    QStyle,
    QTabBar,
    QStyleOptionTab,
)


class CustomTabBar(QTabBar):
    def __init__(self):
        QTabBar.__init__(self)
        self.setContentsMargins(0, 0, 0, 0)


    def tabSizeHint(self, index):
        size = super().tabSizeHint(index)
        w = size.width() + 80
        h = size.height() + 15
        return QSize(w, h)