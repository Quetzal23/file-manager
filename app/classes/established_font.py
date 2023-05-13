import os

from PyQt5.QtGui import ( QFontDatabase, )


class EstablishedFont:
    def __init__(self, font_path):
        self._font_path = font_path


    def get_font_families(self):
        obj_fonts = []
        with os.scandir(self._font_path) as fonts:
            ffont = [font.name for font in fonts if font.is_file()]
        for font in ffont:
            path = os.path.join(self._font_path, font)
            _id = QFontDatabase.addApplicationFont(path)
            family = QFontDatabase.applicationFontFamilies(_id)
            obj_fonts.append(family[0])
        return obj_fonts