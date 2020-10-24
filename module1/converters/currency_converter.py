from module1.common import *


class CurrencyConverter(Common):
    def __init__(self):
        super(CurrencyConverter, self).__init__()

    def convert_currency(self, currency_in, currency_to):
        if type(currency_in) not in [int, float]:
            try:
                currency_in = float(currency_in)
            except:
                print('Incorrect currency value, please type it correctly')
                return None

        if currency_to.lower() == 'u':
            exchange_rate = self.__get_exchange_rate(currency_to)
            return self.__convert_pln_to_usd(currency_in, exchange_rate)

        elif currency_to.lower() == 'p':
            exchange_rate = self.__get_exchange_rate(currency_to)
            return self.__convert_usd_to_pln(currency_in, exchange_rate)

        else:
            print('Incorrect currency system selection, please select it correctly')
            return None

    @staticmethod
    def __convert_pln_to_usd(currency_in, exchange_rate):
        return currency_in*exchange_rate

    @staticmethod
    def __convert_usd_to_pln(currency_in, exchange_rate):
        return currency_in*exchange_rate

    def __get_exchange_rate(self, currency_to):
        if currency_to.lower() == 'u':
            url_pln_usd = r'https://transferwise.com/gb/currency-converter/pln-to-usd-rate'
            pln_usd = self.http_get(url_pln_usd, auto_parse=True)
            pln_usd = self.__extract_exchange_pln_usd(pln_usd)
            return pln_usd

        elif currency_to.lower() == 'p':
            url_usd_pln = r'https://www.bankier.pl/waluty/kursy-walut/forex/USDPLN'
            usd_pln = self.http_get(url_usd_pln, auto_parse=True)
            usd_pln = self.__extract_exchange_usd_pln(usd_pln)
            return usd_pln

    @staticmethod
    def __extract_exchange_usd_pln(soup):
        exchange = soup.find('div', {'class': 'profilLast'}).text
        exchange = float(exchange.replace(',', '.'))
        return exchange

    @staticmethod
    def __extract_exchange_pln_usd(soup):
        exchange = soup.find('span', {'class': 'text-success'}).text
        exchange = float(exchange.replace(',', '.'))
        return exchange

