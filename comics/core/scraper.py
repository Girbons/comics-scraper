import os
import re
import shutil

import cfscrape
import requests

from bs4 import BeautifulSoup

from .settings import configuration


class Scraper:
    def __init__(self, url):
        self.url = url

    def scrape_comic(self):
        """
        Get page raw content
        """
        scraper = cfscrape.create_scraper()
        response = scraper.get(self.url)
        return self.handle_response(response)

    def handle_response(self, response):
        """
        Evaluate response status code
        """
        status_code = response.status_code
        if 200 <= status_code <= 299:
            return response
        else:
            raise('Something went wrong - Status code: {}'.format(status_code))

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
