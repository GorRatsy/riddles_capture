import requests
import json
from bs4 import BeautifulSoup

def get_riggles(n:int, url='https://jservice.io/api/random?count=') -> list:
    r = requests.get(url+str(n))

    try:
        soup = BeautifulSoup(r.text, 'html.parser')
        data = json.loads(soup.text)

        return data

    except AttributeError:
        print('Connection failure. Check your internet connection or inserted url.')