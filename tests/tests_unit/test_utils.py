import os

from comics.utils import create_and_change_dir, is_url_valid


def test_create_and_change():
    create_and_change_dir('test_dir')
    current_wd = os.getcwd()
    assert 'test_dir' in current_wd
    os.removedirs(current_wd)


def test_valid_url():
    assert is_url_valid('http://example.com') is True
    assert is_url_valid('http://foo.gif') is False
    assert is_url_valid('aaaaaa') is False
