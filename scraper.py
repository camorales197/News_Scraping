
def prepare_scraper(url, wanted_list):
    from autoscraper import AutoScraper
    scraper = AutoScraper()
    result = scraper.build(url, wanted_list)
    return scraper

def scraping(url, scraper):
    results = scraper.get_result_similar(url)
    return results





