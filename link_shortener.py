import os

from pathlib import Path
from urllib.parse import urlparse

import requests


def is_bitlink(url: str) -> str:
    '''the function returns the number of clicks on the bitlink.
    If there is no such bitlink, the bitlink will be returned.'''
    if urlparse(url)[1] == 'bit.ly' or urlparse(url)[1] == 'www.bit.ly':
        return f'Clicks count: {get_click_count(BITLINK_TOKEN, url)}'
    else:
        return f'Bitlink created: {get_shorten_link(BITLINK_TOKEN, url)}'


def get_click_count(token: str, url: str) -> int:
    '''Function returns click count all time for bitlink'''

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    api_link = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'
    request_link = api_link.format(urlparse(url)[1] + urlparse(url)[2])
    bitly_response = requests.get(request_link, headers=headers)
    bitly_response.raise_for_status()
    return bitly_response.json()['total_clicks']


def get_shorten_link(token: str, url: str) -> str:
    '''Function returns shortern link'''

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    data = {'long_url': url}

    bitly_response = requests.post(
        'https://api-ssl.bitly.com/v4/bitlinks',
        headers=headers,
        json=data
        )
    bitly_response.raise_for_status()
    return bitly_response.json()['link']


if __name__ == '__main__':

    env_path = Path('.') / '.env'
    BITLINK_TOKEN = os.getenv('BITLINK_TOKEN')

    print(is_bitlink(url=input(f'Paste bitlink/url here: ').strip()))
