class StylesSheet:
    def __init__(self, style_file):
        self._style_file = style_file


    def stylesheet(self):
        with open(self._style_file, 'r') as file:
            return file.read()