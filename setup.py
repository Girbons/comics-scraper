from setuptools import setup, find_packages


LONG_DESCRIPTION = open('README.md').read()


setup(
    name="comics-scraper",
    version=0.4,
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
