import os
import subprocess

import pytest


def test_readcomiconlineto():
    """
    Test download from http://readcomiconline.to/
    """
    subprocess.call([
        'comics-download', '-u', 'http://readcomiconline.to/Comic/X-Factor-1986/Issue-12?id=40621&readType=1'
    ])
    assert os.path.isfile("downloaded_comics/ReadComicOnline/X-Factor-1986/12.pdf")


@pytest.mark.skip(reason='Apparently offline')
def test_readcomicsio():
    """
    Test download from https://readcomics.io/
    """
    subprocess.call([
        'comics-download', '-u', 'https://readcomics.io/old-man-logan/chapter-38/full'
    ])
    assert os.path.isfile("downloaded_comics/ReadComics/old-man-logan/chapter-38.pdf")


def test_readcomicextra():
    """
    Test download from http://comicextra.com/
    """
    subprocess.call([
        'comics-download', '-u', 'http://www.comicextra.com/daredevil-2016/chapter-600/full'
    ])
    assert os.path.isfile("downloaded_comics/ComicExtra/daredevil-2016/chapter-600.pdf")


def test_mangareader():
    """
    Test download from https://www.mangareader.net/
    """
    subprocess.call([
        'comics-download', '-u', 'https://www.mangareader.net/naruto/1'
    ])
    assert os.path.isfile("downloaded_comics/MangaReader/naruto/1.pdf")


def test_mangahere():
    """
    Test download from http://mangahere.cc
    """
    subprocess.call([
        'comics-download', '-u', 'http://www.mangahere.cc/manga/shingeki_no_kyojin_before_the_fall/c048/'
    ])
    assert os.path.isfile("downloaded_comics/MangaHere/shingeki_no_kyojin_before_the_fall/c048.pdf")
