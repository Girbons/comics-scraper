import os

import requests


from comics.utils import get_images_link, create_and_change_dir


def test_images_link():
    response = requests.get('http://www.comicextra.com/daredevil-2016/chapter-600/full')
    regex = '<img[^>]+src="([^">]+)"'
    links = get_images_link(response, regex)

    assert len(links) == 45


def test_create_and_change():
    create_and_change_dir('test_dir')
    current_wd = os.getcwd()
    assert 'test_dir' in current_wd
    os.removedirs(current_wd)
