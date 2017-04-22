import glob
import os
import re
import shutil
import img2pdf

import cfscrape
import click
import requests

from bs4 import BeautifulSoup
from natsort import natsorted
from PIL import Image


SESSION = requests.Session()


def download_image(image_url, image_name, name):
    response = SESSION.get(image_url, stream=True)
    if response.status_code is not 200:
        raise 'Cannot download image'
    if not os.path.exists('comics'):
        os.makedirs('comics')
    dir_name = '{}-pages'.format(name)
    if not os.path.exists('comics/{}'.format(dir_name)):
        os.makedirs('comics/{}'.format(dir_name))
    with open(os.path.join('comics/{}'.format(dir_name), image_name), 'wb') as f:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f)


def make_pdf(name):
    dir_name = '{}-pages'.format(name)
    os.chdir('comics/{}'.format(dir_name))
    images = [image for image in glob.glob('*.jpg')]
    sorted_img = natsorted(images)
    comic_pdf = '{}.pdf'.format(name)
    with open(comic_pdf, 'wb') as f:
        f.write(img2pdf.convert(sorted_img))


@click.command()
@click.option('--url', '-u', default='', help='comic link')
@click.option('--name', '-n', default='', help='comic name')
def comic(url, name):
    scraper = cfscrape.create_scraper()
    response = scraper.get(url)
    if response.status_code is not 200:
        raise 'Something went wrong, check the url or your connection'
    soup = BeautifulSoup(response.content, 'html.parser')
    links = re.findall('stImages.push\(\"(.*?)\"\)\;', str(soup))
    for number, link in enumerate(links):
        image_name = '{}.jpg'.format(number)
        download_image(link, image_name, name)
    make_pdf(name)


if __name__ == '__main__':
    comic()
