from scraper import *

url_train = 'https://www.elperiodicoextremadura.com/noticias/extremadura/claves-saber-si-terraza-invierno-debe-estar-' \
      '40-50-aforo_1260164.html'

url1 = 'https://www.elperiodicoextremadura.com/noticias/extremadura/' \
       'como-funcionan-nuevos-test-covid-farmaciaseuros_1260171.html'


if __name__ == '__main__':
    scraper = prepare_scraper(url_train)
    scraping(url1, scraper)
