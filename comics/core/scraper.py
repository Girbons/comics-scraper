import click
import cfscrape
import requests


class Scraper:

    def __init__(self, url):
        self.url = url
        self._scraper = cfscrape.create_scraper()

    def scrape_comic(self, antibot):
        """
        Get page raw content
        """
        if antibot:
            response = self._scraper.get(self.url)
        else:
            response = requests.get(self.url)

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
