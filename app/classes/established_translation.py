import gettext


class EstablishedTranslation:
    def __init__(self, app_name, lang_path, lang_current):
        self._app_name = app_name
        self._lang_path = lang_path
        self._lang_current = lang_current


    def gettext(self):
        gettext.bindtextdomain(self._app_name, self._lang_path)
        gettext.textdomain(self._app_name)
        lang = gettext.translation(self._app_name, localedir=self._lang_path, languages=[self._lang_current], fallback=True)
        lang.install()