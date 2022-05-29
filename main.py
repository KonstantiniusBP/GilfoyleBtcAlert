import requests
from bs4 import BeautifulSoup
import time

crypto_url = 'https://www.binance.com/ru/price/bitcoin'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}

def crypto_tracker():
    html_page = requests.get(crypto_url, headers=headers)
    soup = BeautifulSoup(html_page.content, 'html.parser')
    crypto_price = soup.findAll("div", {"class": "css-12ujz79"})
    print(crypto_price[0].text)
    time.sleep(5)
    crypto_tracker()
crypto_tracker()