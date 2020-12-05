from autoscraper import AutoScraper

def prepare_scraper(url):
    wanted_list = ["Claves para saber si una terraza de invierno debe estar al 40% o al 50% del aforo"]
    scraper = AutoScraper()
    result = scraper.build(url, wanted_list)
    return scraper

def scraping(url, scraper):
    results = scraper.get_result_similar(url)
    print(results)
