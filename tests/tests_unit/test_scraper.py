from comics.core.scraper import Scraper


def test_scraper():
    scraper = Scraper('http://example.com')
    response = scraper.scrape_comic(False)
    assert response.status_code == 200


def test_scraper_antibot():
    scraper = Scraper('http://example.com')
    response = scraper.scrape_comic(True)
    assert response.status_code == 200
