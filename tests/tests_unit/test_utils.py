import os


from comics.utils import create_and_change_dir


def test_create_and_change():
    create_and_change_dir('test_dir')
    current_wd = os.getcwd()
    assert 'test_dir' in current_wd
    os.removedirs(current_wd)
