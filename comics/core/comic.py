import glob
import os
import re
import shutil

import img2pdf

from natsort import natsorted

from .settings import configuration


class Comic:
    def __init__(self, url):
        self.url = url.split('/')
        self.name = self.url[4]
        self.issue_number = re.findall(configuration['issue_number'], self.url[5])[0]

    def check_comic(self):
        """
        Check if comic folder and file is present
        """
        if os.path.exists(self.name):
            os.chdir(self.name)
            os.path.isfile(self.issue_number)
        else:
            return False

    def make_pdf(self):
        """
        From downloaded images make a pdf
        """
        images = [image for image in glob.glob('images/*.jpg')]
        sorted_img = natsorted(images)
        comic_pdf = '{}.pdf'.format(self.issue_number)
        if not os.path.exists(self.name):
            os.mkdir(self.name)
        with open(comic_pdf, 'wb') as f:
            f.write(img2pdf.convert(sorted_img))
        shutil.move(comic_pdf, '{}/{}'.format(self.name, comic_pdf))
        shutil.rmtree('images')
