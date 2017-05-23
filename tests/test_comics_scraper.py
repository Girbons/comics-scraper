import os
import subprocess


def test_comics_scraper():
    os.chdir("comics")
    subprocess.call([
        'python', 'downloader.py', '-u', 'http://readcomiconline.to/Comic/X-Factor-1986/Issue-12?id=40621&readType=1'
    ])
    assert os.path.exists("downloaded_comics/X-Factor-1986")
    assert os.path.isfile("downloaded_comics/X-Factor-1986/12.pdf")
