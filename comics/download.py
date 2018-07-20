import click

from .core.downloader import Downloader


@click.command()
@click.option('--url', '-u', required=True, help='comics url')
def download(url):
    Downloader(url).run()


if __name__ == "__main__":
    download()
