import sys

import click

from core.comic import Comic
from core.scraper import Scraper


@click.command()
@click.option('--url', '-u', default='', help='comic url')
def get_comic(url):
    if not url:
        raise Exception('No url inserted')
    if 'readcomiconline.to' not in url:
        raise Exception('Invalid url')
    comic = Comic(url)
    if not comic.check_comic():
        scraper = Scraper(url)
        scraper.runner()
        comic.make_pdf()
        print("Download completed, comic available in comics/downloaded_comics/{}".format(comic.name))
    else:
        print("Comic already present")
        sys.exit()


if __name__ == "__main__":
    get_comic()
