from setuptools import setup, find_packages

import os
import re


def get_version(package):
    """
    Return package version as listed in `__version__` in `__init__.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


LONG_DESCRIPTION = open('README.md').read()

version = get_version('comics')


setup(
    name="comics-downloader",
    version=version,
    author="Alessandro De Angelis",
    author_email="alessandrodea22@gmail.com",
    description="comics scraper",
    long_description=LONG_DESCRIPTION,
    license="MIT",
    keywords="comics scraper",
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'backports.tempfile',
        'click',
        'cfscrape',
        'bs4',
        'img2pdf',
        'natsort',
        'requests',
        'validators',
        'tqdm',
    ],
    entry_points='''
        [console_scripts]
        comics-download=comics.download:download
    '''
)
