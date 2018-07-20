import re

import requests

from bs4 import BeautifulSoup

from ..core.comics import BaseComics


class MangaReader(BaseComics):
    """
    class for https://www.mangareader.net/
    """
    def __init__(self, url):
        self.base_url = 'https://www.mangareader.net'
        self._image_regex = '<img[^>]+src="([^">]+)"'
        self.antibot = False
        super(MangaReader, self).__init__(url)

    @property
    def name(self):
        return self.splitted_url[3]

    @property
    def issue_number(self):
        return self.splitted_url[4]

    def images_links(self, response):
        session = requests.Session()
        soup = BeautifulSoup(response.content, 'html.parser')
        # retrieve the <options> in page
        options = soup.findAll('option')
        links = []

        for option in options:
            links.append('{}{}'.format(self.base_url, option['value']))

        images_links = []
        for link in links:
            response = session.get(link)
            # we'll find only 1 image
            image_url = re.findall(self._image_regex, response.text)[0]
            images_links.append(image_url)

        return images_links
