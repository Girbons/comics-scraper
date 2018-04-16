import glob
import os
import shutil
import tempfile

import requests
import img2pdf

from natsort import natsorted

from .scraper import Scraper

from ..settings import comics_settings
from ..utils import create_and_change_dir, get_images_link


class BaseComics:

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

    def make_pdf(self):
        """
        Download images and makes a pdf
        """
        # scrape the page and download the images
        response = self.scraper.scrape_comic(self.antibot)

        links = get_images_link(response, self._image_regex)

        # we are going to make several requests to the same host
        session = requests.Session()

        # here we use a temporary directory to download the images
        # once out of the context the temp folder will be automatically removed
        with tempfile.TemporaryDirectory() as temp_dir:
            for n, link in enumerate(links):
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
