import requests
from bs4 import BeautifulSoup
import time
import json

crypto_url = 'https://api.coincap.io/v2/assets/bitcoin'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}

def crypto_tracker():
    html_responce = requests.get(crypto_url, headers=headers)
    json_data = html_responce.json()
    print(json_data['data']['priceUsd'])
    time.sleep(5)
    crypto_tracker()
crypto_tracker()