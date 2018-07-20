from ..core.comics import BaseComics


class ReadComics(BaseComics):
    """
    class for https://readcomics.io
    """
    def __init__(self, url):
        self._image_regex = '<img[^>]+src="([^">]+)"'
        self.antibot = False
        super(ReadComics, self).__init__(url)

    @property
    def name(self):
        # here we split the url
        # so the result will be
        # ['protocol', '', 'domain', 'title'...]
        return self.splitted_url[3]

    @property
    def issue_number(self):
        return self.splitted_url[4]
