import re


from ..core.comics import BaseComics


class ReadComicOnline(BaseComics):
    """
    class for http://readcomiconline.to/
    """
    def __init__(self, url):
        self._issue_number_regex = r'[(\d)]+'
        self._image_regex = 'stImages.push\(\"(.*?)\"\)\;'
        self.antibot = True
        super(ReadComicOnline, self).__init__(url)

    @property
    def name(self):
        return self.splitted_url[4]

    @property
    def issue_number(self):
        return re.findall(self._issue_number_regex, self.splitted_url[5])[0]
