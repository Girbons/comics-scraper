import glob
import os
import re
import shutil


import requests
import img2pdf

from bs4 import BeautifulSoup
from tqdm import tqdm
from natsort import natsorted

from .scraper import Scraper

from ..compat import TemporaryDirectory
from ..settings import comics_settings
from ..utils import create_and_change_dir, is_url_valid


class BaseComics(object):

    def __init__(self, url):
        self.url = url
        self.scraper = Scraper(url)
        self.splitted_url = url.split('/')

    @property
    def name(self):
        msg = 'Please define how to retrieve the name.'
        raise NotImplementedError(msg)

    @property
    def issue_number(self):
        msg = 'Please define how to retrieve the issue number.'
        raise NotImplementedError(msg)

    def images_links(self, response):
        """
        :param response: is the response instance.

        from a response content extract images link
        and return a list of link
        exclude .gif
        """
        soup = BeautifulSoup(response.content, 'html.parser')
        match = re.findall(self._image_regex, str(soup))
        links = []

        for link in match:
            if is_url_valid(link):
                links.append(link)

        return links

    def make_pdf(self):
        """
        Makes a pdf
        """
        # scrape the page and download the images
        response = self.scraper.scrape_comic(self.antibot)
        # we are going to make several requests to the same host
        session = requests.Session()
        # retrieve all the images links to download
        links = self.images_links(response)
        # here we use a temporary directory to download the images
        # once out of the context the temp folder will be automatically removed
        with TemporaryDirectory() as temp_dir:
            for n, link in enumerate(tqdm(links)):
                response = session.get(link, stream=True)
                with open(os.path.join(temp_dir, '{}.jpg'.format(n)), 'wb') as f:
                    response.raw.decode_content = True
                    shutil.copyfileobj(response.raw, f)

            # regroup all the images into a list so we can sort them
            # to avoid a bad pagination
            images = [image for image in glob.glob('{}/*.jpg'.format(temp_dir))]
            sorted_img = natsorted(images)
            # build comic name
            comic_pdf = '{}.pdf'.format(self.issue_number)

            os.chdir(comics_settings.path)
            create_and_change_dir(self.__class__.__name__)
            create_and_change_dir(self.name)

            # create the pdf file from the images
            with open(comic_pdf, 'wb') as f:
                f.write(img2pdf.convert(sorted_img))

            print('Comic successfully downloaded')
