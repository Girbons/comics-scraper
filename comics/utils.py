import os

import validators


def create_and_change_dir(dir_name):
    """
    :param string dir_name: is the folder name.

    create a directory if does not exist and change to it
    """
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    os.chdir(dir_name)


def is_url_valid(url):
    """
    :param string url: is a url

    check if the given url is valid and is not a gif
    """
    if not url.endswith('.gif') and validators.url(url):
        return True

    return False
