import requests
from bs4 import BeautifulSoup
from currency_converter import CurrencyConverter
import ssl
import urllib.request


def get_exchange_rate(target1, target2):
    headers = {"User-Agent": "Mozilla/5.o", "Content-Type": "text/html; charset=utf-8"}

    response = requests.get(
        "https://kr.investing.com/currencies/{}-{}".format(target1, target2),
        headers=headers,
    )
    content = BeautifulSoup(response.content, "html.parser")
    containers = content.find("span", {"data-test": "instrument-price-last"})
    print(containers.text)


ssl._create_default_https_context = ssl._create_unverified_context
cc = CurrencyConverter("http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip")
# print(cc.currencies)
print(cc.convert(1, "USD", "KRW"))

get_exchange_rate("usd", "krw")
