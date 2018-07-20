import os

try:
    from urllib.parse import urlsplit
except ImportError:
    from urlparse import urlsplit

from ..exceptions import SiteNotSupported
from ..settings import comics_settings, SUPPORTED_SITES


class Downloader(object):
    """
    Downloader is used to detect the specific class to use to download the comic.
    """
    def __init__(self, url):
        self.url = url

    def create_default_folder(self):
        if not os.path.exists(comics_settings.path):
            os.mkdir(comics_settings.path)

    def load_class(self):
        """
        From the domain return the specific class to use to download
        the comics.
        """
        # for example we have http://example.com
        # the netloc part is `example.com`
        domain = urlsplit(self.url).netloc

        if 'www' in domain:
            domain = domain[4:]

        if domain not in SUPPORTED_SITES:
            msg = '{} is not supported yet, please open an issue to add it.'.format(domain)
            raise SiteNotSupported(msg)

        return getattr(comics_settings, domain)

    def run(self):
        klass = self.load_class()
        self.create_default_folder()
        klass(self.url).make_pdf()
