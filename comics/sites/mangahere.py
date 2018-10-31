import re

import requests

from bs4 import BeautifulSoup

from ..core.comics import BaseComics
from ..utils import is_url_valid


class MangaHere(BaseComics):
    """
    class for http://www.mangahere.cc/
    """
    def __init__(self, url):
        self.base_url = 'http://www.mangahere.cc/'
        self._image_regex = r'<img[^>]+src="([^">]+)"'
        self.antibot = False
        super(MangaHere, self).__init__(url)

    @property
    def name(self):
        return self.splitted_url[4]

    @property
    def issue_number(self):
        return self.splitted_url[5]

    def images_links(self, response):
        session = requests.Session()
        soup = BeautifulSoup(response.content, 'html.parser')
        # retrieve the <options> in page
        options = soup.findAll('option')
        links = []

        for option in options:
            links.append('http:{}'.format(option['value']))

        images_links = []
        for link in links:
            response = session.get(link)
            image_url = re.findall(self._image_regex, response.text)[1]
            if is_url_valid(image_url):
                images_links.append(image_url)

        return images_links
