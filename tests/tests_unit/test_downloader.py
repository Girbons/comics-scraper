import os
import pytest

from comics.core.downloader import Downloader
from comics.exceptions import NotSupportedSite

from comics.sites.comicextra import ComicExtra
from comics.settings import comics_settings


def test_downloader_not_supported_site():
    dl = Downloader('http://example.com')

    with pytest.raises(NotSupportedSite) as ex_info:
        dl.load_class()
    assert 'example.com is not supported yet.' in str(ex_info.value) # noqa


def test_downloader_load_class():
    """
    Test load_class() method with a site that starts with `www`
    """
    dl = Downloader('http://www.comicextra.com/daredevil-2016/chapter-600/full')
    klass = dl.load_class()
    assert klass == ComicExtra


def test_downloader_run():
    dl = Downloader('http://www.comicextra.com/daredevil-2016/chapter-600/full')
    dl.run()
    assert os.path.isfile('chapter-600.pdf')


def test_downloader_create_default_folder():
    """
    Downloader must create the folder defined in settings
    """
    dl = Downloader('http://fake.url')
    dl.create_default_folder()
    default_dir = '{}/{}'.format(os.getcwd(), comics_settings.path)

    assert os.path.exists(default_dir)
