import os
import subprocess


def test_readcomiconlineto():
    """
    Test download from http://readcomiconline.to/
    """
    os.chdir("comics")
    subprocess.call([
        'python', 'download.py', '-u', 'http://readcomiconline.to/Comic/X-Factor-1986/Issue-12?id=40621&readType=1'
    ])
    assert os.path.isfile("downloaded_comics/ReadComicOnline/X-Factor-1986/12.pdf")


def test_readcomicsio():
    """
    Test download from https://readcomics.io/
    """
    subprocess.call([
        'python', 'download.py', '-u', 'https://readcomics.io/old-man-logan/chapter-38/full'
    ])
    assert os.path.isfile("downloaded_comics/ReadComics/old-man-logan/chapter-38.pdf")
