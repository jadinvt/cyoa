class Page(object):
    """The central object is the page which provides text and a list of 
        attached pages_"""
    def __init__(self, name ="Unnamed Room", text="No description for this page", choices=None):
        self._text = text
        if choices==None:
            choices = []
        else:
            self._choices = choices
    def set_text(self, text):
        self._text = text

    def get_text(self):
        return(self._text)

    def set_choices(self, choices):
        self._choices = choices

    def get_choices(self):
        return(_choices)


