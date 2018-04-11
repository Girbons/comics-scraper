import os
import re
import shutil

import click
import cfscrape
import requests

from bs4 import BeautifulSoup

from .settings import configuration


class Scraper:
    def __init__(self, url):
        self.url = url
        self._scraper = cfscrape.create_scraper()

    def scrape_comic(self):
        """
        Get page raw content
        """
        response = self._scraper.get(self.url)
        return self.handle_response(response)

    def handle_response(self, response):
        """
        Evaluate response status code
        """
        try:
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            raise click.ClickException(str(e))

    def get_images_links(self, response):
        """
        Extract images links from parsed content
        """
        soup = BeautifulSoup(response.content, 'html.parser')
        return re.findall(configuration['images'], str(soup))

    def download_images(self, links):
        if not os.path.exists('downloaded_comics'):
            os.mkdir('downloaded_comics')
        os.chdir('downloaded_comics')
        if not os.path.exists('images'):
            os.mkdir('images')
        session = requests.Session()
        for n, link in enumerate(links):
            response = session.get(link, stream=True)
            with open(os.path.join('images', '{}.jpg'.format(n)), 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)

    def runner(self):
        response = self.scrape_comic()
        links = self.get_images_links(response)
        self.download_images(links)
