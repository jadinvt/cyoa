class Choice(object):
    def __init__(self, text="textless choice", destination=None):
        """Initialization of Choice object"""
        self._text = text
        self._destination = destination
    def set_text(self, text):
        self._text = text
    def get_text(self):
        return(self._text)
    def set_destination(self, destination):
        self._destination = destination
    def get_destination(self, destination):
        return(self._destination)


