import requests
from bs4 import BeautifulSoup as bs
from dateutil.parser import parse
from pprint import pprint

def get_exchange_list_xrates(currency, amount=1):
    # делаем запрос на x-rates.com, чтобы получить актуальные курсы обмена распространенных валют
    content = requests.get(f"https://www.x-rates.com/table/?from={currency}&amount={amount}").content
    # инициализируем beautifulsoup
    soup = bs(content, "html.parser")
    # получить таблицы курсов валют
    exchange_tables = soup.find_all("table")
    exchange_rates = {}
    for exchange_table in exchange_tables:
        for tr in exchange_table.find_all("tr"):
            # for each row in the table
            tds = tr.find_all("td")
            if tds:
                currency = tds[0].text
                # получаем курс обмена
                exchange_rate = float(tds[1].text)
                exchange_rates[currency] = exchange_rate
    return exchange_rates


def get_exchange_usd_rates(currency, amount=1):
    # делаем запрос на x-rates.com, чтобы получить актуальные курсы обмена распространенных валют
    content = requests.get(f"https://www.x-rates.com/table/?from={currency}&amount={amount}").content
    # инициализируем beautifulsoup
    soup = bs(content, "html.parser")
    # получить таблицы курсов валют
    exchange_tables = soup.find_all("table")
    exchange_rates = {}
    for exchange_table in exchange_tables:
        for tr in exchange_table.find_all("tr"):
            # for each row in the table
            tds = tr.find_all("td")
            if tds:
                currency = tds[0].text
                if currency == 'US Dollar':
                # получаем курс обмена
                    exchange_rate = float(tds[1].text)
                    exchange_rates[currency] = exchange_rate
                else:
                    continue
    return exchange_rates


def usd_converter(convert_from, amount, convert_to='USD'):
    url = f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={convert_from}&To={convert_to}"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
    page = requests.get(url=url, headers=headers)
    return bs(page.text, 'html.parser')


def get_exchange(data):
    currency_container = data.findAll('p', class_='sc-814e9b01-1 hTlWRC')
    for price in currency_container:
        usd = price.text.split()[0]
        usd = usd.split('.')[0]
        if len(usd) > 3:
            usd = usd.replace(',', '')
            return int(usd)
        else:
            return int(usd)


def main():
    get_exchange(usd_converter(convert_from='RUB', amount=3665600))


if __name__ == '__main__':
    main()


