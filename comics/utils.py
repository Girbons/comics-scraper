import os
import re

import validators

from bs4 import BeautifulSoup


def create_and_change_dir(dir_name):
    """
    :param string dir_name: is the folder name.

    create a directory if does not exist and change to it
    """
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    os.chdir(dir_name)


def get_images_link(response, image_regex):
    """
    :param response: is the response instance.
    :param image_regex: is the image regex

    from a response contet extract images link
    and return a list of link
    exclude .gif
    """
    soup = BeautifulSoup(response.content, 'html.parser')
    match = re.findall(image_regex, str(soup))
    links = []

    for link in match:
        if not link.endswith('.gif') and validators.url(link):
            links.append(link)

    return links
