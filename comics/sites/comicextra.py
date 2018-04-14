from ..core.comic import BaseComic


class ComicExtra(BaseComic):
    """
    class for http://www.comicextra.com/
    """
    def __init__(self, url):
        self._image_regex = '<img[^>]+src="([^">]+)"'
        self.antibot = False
        super().__init__(url)

    @property
    def name(self):
        return self.splitted_url[3]

    @property
    def issue_number(self):
        return self.splitted_url[4]
