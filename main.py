from scraper import *
import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Starting the script')

url_train = 'https://www.elperiodicoextremadura.com/noticias/extremadura/claves-saber-si-terraza-invierno-debe-estar-' \
      '40-50-aforo_1260164.html'

url1 = 'https://www.elperiodicoextremadura.com/noticias/extremadura/' \
       'como-funcionan-nuevos-test-covid-farmaciaseuros_1260171.html'

wanted_list = ["Claves para saber si una terraza de invierno debe estar al 40% o al 50% del aforo"]


if __name__ == '__main__':
    logging.debug('Starting "prepare_scraper"')
    scraper = prepare_scraper(url_train, wanted_list)
    logging.debug('Starting "scraping"')
    scraping(url1, scraper)
    logging.debug('Script finished well')

