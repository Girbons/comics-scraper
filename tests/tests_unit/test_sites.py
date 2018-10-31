import os
import pytest

from comics.core.comics import BaseComics

from comics.sites import (
    ComicExtra,
    ReadComics,
    ReadComicOnline,
    MangaHere,
    MangaReader,
)


def test_base_comic():
    comics = BaseComics('')

    with pytest.raises(NotImplementedError) as ex_info:
        comics.name
    assert 'Please define how to retrieve the name.' in str(ex_info)

    with pytest.raises(NotImplementedError) as ex_info:
        comics.issue_number
    assert 'Please define how to retrieve the issue number.' in str(ex_info)


def test_comicextra():
    url = 'http://www.comicextra.com/daredevil-2016/chapter-600/full'
    comics = ComicExtra(url)
    comics.make_pdf()

    assert comics.name == 'daredevil-2016'
    assert comics.issue_number == 'chapter-600'
    assert os.listdir(os.getcwd()) == ['chapter-600.pdf']


def test_readcomiconline():
    url = 'http://readcomiconline.to/Comic/X-Factor-1986/Issue-12\?id\=40621\&readType\=1'
    comics = ReadComicOnline(url)

    assert comics.name == 'X-Factor-1986'
    assert comics.issue_number == '12'


def test_readomicsio():
    url = 'https://readcomics.io/old-man-logan/chapter-38/full'
    comics = ReadComics(url)

    assert comics.name == 'old-man-logan'
    assert comics.issue_number == 'chapter-38'


def test_mangareader():
    url = 'https://www.mangareader.net/naruto/1'
    comics = MangaReader(url)
    response = comics.scraper.scrape_comic(False)
    result = comics.images_links(response)

    assert comics.name == 'naruto'
    assert comics.issue_number == '1'
    assert len(result) == 53


def test_mangahere():
    url = 'http://www.mangahere.cc/manga/shingeki_no_kyojin_before_the_fall/c048/'
    comics = MangaHere(url)
    response = comics.scraper.scrape_comic(False)
    result = comics.images_links(response)

    assert comics.name == 'shingeki_no_kyojin_before_the_fall'
    assert comics.issue_number == 'c048'
    assert len(result) == 132
