class EstablishedText:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


    def load_file_text(self, file_path):
        self._set_text = {}
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    key, value = line.split(':', 1)
                    self._set_text[key.strip()] = value.strip()
        return self._set_text


    def get_text(self, key):
        try:
            text = _(self._set_text[key])
            return text.replace('\\n', '<br>')
        except KeyError:
            return ''
