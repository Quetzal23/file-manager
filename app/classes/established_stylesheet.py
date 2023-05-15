class EstablishedStylesheet:
    def __init__(self, file_style):
        self._file_style = file_style


    def stylesheet(self):
        with open(self._file_style, 'r') as file:
            return file.read()
