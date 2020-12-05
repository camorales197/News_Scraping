from autoscraper import AutoScraper

def prepare_scraper(url):
    wanted_list = ["Claves para saber si una terraza de invierno debe estar al 40% o al 50% del aforo"]
    scraper = AutoScraper()
    return scraper

def scraping(url, scraper):
    results = scraper.get_result_similar(url)
    print(results)

url = 'https://www.elperiodicoextremadura.com/noticias/extremadura/claves-saber-si-terraza-invierno-debe-estar-' \
      '40-50-aforo_1260164.html'
scraper = prepare_scraper(url)



url1 = 'https://www.elperiodicoextremadura.com/noticias/extremadura/extremenos-elevan-40-ocupacion-norte-caceres-' \
       'puente-localidades-100_1260248.html'
url2 = 'https://www.elperiodicoextremadura.com/noticias/extremadura/extremadura-lamenta-seis-fallecidos-covid-183-' \
       'contagios-ultima-jornada_1260247.html'
url3 = 'https://www.elperiodicoextremadura.com/noticias/extremadura/como-funcionan-nuevos-test-covid-farmaciaseuros_' \
       '1260171.html'

scraping(url2, scraper)


