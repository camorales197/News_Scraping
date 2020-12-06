from scraper import prepare_scraper, scraping


url_train = 'https://www.elperiodicoextremadura.com/noticias' \
            '/extremadura/claves-saber-si-terraza-' \
            'invierno-debe-estar-40-50-aforo_1260164.html'
url1 = 'https://www.elperiodicoextremadura.com/noticias/' \
       'extremadura/como-funcionan-nuevos-test-' \
       'covid-farmaciaseuros_1260171.html'
wanted_list = ["Claves para saber si una terraza de i"
               "nvierno debe estar al 40% o al 50% del aforo"]

scraper = prepare_scraper(url_train, wanted_list)


def test_prepare_scrapper(url=url_train, wanted_list=wanted_list):
    scraper = prepare_scraper(url, wanted_list)
    result = scraper.build(url, wanted_list)
    assert result == ['Claves para saber si una terraza '
                      'de invierno debe estar al 40% o al 50% del aforo']


def test_scraping(url=url1, scraper=scraper):
    results = scraping(url, scraper)
    assert results == ['¿Cómo funcionan los nuevos '
                       'test covid de las farmacias?']
