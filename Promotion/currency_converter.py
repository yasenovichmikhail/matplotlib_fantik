import requests
from bs4 import BeautifulSoup as bs
from dateutil.parser import parse
from pprint import pprint


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
        if len(usd) > 3:
            usd = usd.replace(',', '')
            return round(float(usd), 2)
        else:
            return round(float(usd), 2)


def main():
    get_exchange(usd_converter(convert_from='AED', amount=5000.89))


if __name__ == '__main__':
    main()


